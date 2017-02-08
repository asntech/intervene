# coding: utf-8

"""
InterVene: a tool for intersection and visualization of multiple genomic region sets
Created on January 10, 2017
@author: <Aziz Khan>aziz.khan@ncmm.uio.no
"""
import os
import sys
import collections
import time
import os.path as op
import pybedtools
from pybedtools import BedTool
import matplotlib as mp
import numpy as np
import pandas as pd
import pylab as pl
import scipy.cluster.hierarchy as sch
import string
from matplotlib import gridspec


def get_name(fname):
    return op.splitext(op.basename(fname))[0]

def actual_intersection(a, b):
    return len(a.intersect(b, u=True))

def jaccard_of_a(a, b):
    return a.jaccard(b,u=True)['jaccard']

#Calculate the fisher 
def fisher_of_a(a, b, genome):
    return a.fisher(b,genome=genome).two_tail

#Calculate the reldist 
def reldist_of_a(a, b):
    #return mean(a.reldist(b)['reldist'])
    return float(sum(a.reldist(b)['reldist'])) / max(len(a.reldist(b)['reldist']), 1)

def frac_of_a(a, b):
    len_a = float(len(a))
    return len(a.intersect(b, u=True)) / len_a

def enrichment_score(a, b, genome_fn, iterations=1000, processes=1):
    results = a.randomstats(b, new=True, genome_fn=genome_fn, iterations=iterations, processes=processes)
    return (results['actual'] + 1) / (results['median randomized'] + 1)

def create_matrix(beds, func, verbose=False, sort_bed=False, **kwoptions):
    nfiles = len(beds)
    total = nfiles ** 2
    i = 0
    bed_sizes = []
    bed_names = []

    matrix = collections.defaultdict(dict)
    for fa in beds:
        a = BedTool(fa)
        if sort_bed:
            a = a.sort()
        for fb in beds:
            i += 1
            b = BedTool(fb)
            if sort_bed:
                b = b.sort()
            if verbose:
                sys.stderr.write(
                        '%(i)s of %(total)s: %(fa)s + %(fb)s\n' % locals())
                sys.stderr.flush()

            matrix[get_name(fa)][get_name(fb)] = func(a, b, **kwoptions)

        bed_names.append(get_name(fa))
        bed_sizes.append(len(a))
    return matrix, bed_names, bed_sizes



def barplot(series, matrix, outfile, options, max_size=1):
    """Create a bar plot and place the lower triangle of a heatmap directly
    adjacent so that the bases of the bars line up with the diagonal of the
    heatmap. Thanks to Kamil Slowikowski for this code https://gist.github.com/slowkow/5797728

    Parameters
    ----------
    series : pandas.Series
        The bar heights and labels.
    matrix : pandas.DataFrame
        A matrix where each column corresponds to a bar in the bar plot.
    outfile : str
        Full path to the output file.
    figsize : (width, height)
    fontsize : float
    title : str
    """
    # Create a figure.
    fig = pl.figure(figsize=options.figsize)
    gs = gridspec.GridSpec(1, 2, width_ratios=[6, 1]) 

    # Axes for the heatmap triangle.
    ax = fig.add_subplot(gs[0], frame_on=False, aspect=2.0)
    #ax = fig.add_subplot(121, frame_on=False, aspect=2.0)
    
    # Get the heatmap triangle's axes and the order of the clustered samples.
    cax, order = heatmap_triangle(matrix, ax, options.hlabel)

    # Adjust spacing between the heatmap triangle and the barplot.
    #fig.subplots_adjust(wspace=-0.25, hspace=0, left=0, right=1)
    #right=1.1 
    fig.subplots_adjust(wspace=0, hspace=0, left=0, right=options.space)

    # Axes for the barplot.
    #ax = fig.add_subplot(122, frame_on=False)
    ax = fig.add_subplot(gs[1], frame_on=False)

    # Put gridlines beneath the bars.
    ax.set_axisbelow(True)

    # Order the bars by the clustering.
    series = series.ix[order]

    namelen = 15
    # Shorten lengthy names.
    series.index = [shorten(x, namelen) for x in series.index]

    ax = series.plot(ax=ax, kind='barh', title=options.title, linewidth=0,
                     grid=False, color=options.barcolor)

    # Set the font size for the y-axis labels.
    ax.tick_params(axis='y', which='major', labelsize=options.fontsize)

    # Grid lines.
    ax.grid(b=False, which='major', axis='both', alpha=0.1)

    # Tick marks for the x-axis. max(list_size)
    ax.set_xticks((max_size,1))

    # Put the y-axis marks on the right.
    ax.yaxis.tick_right()
    ax.yaxis.set_label_position('right')

    # Adjust tick length.
    ax.tick_params(length=0, axis='x', labelsize=7)
    ax.tick_params(length=0, axis='y')

    # Labels.
    ax.set_xlabel(options.blabel, size=8)
    ax.set_ylabel('')

    fig.tight_layout()

    #fig.show()
    # Save.
    fig.savefig(outfile, bbox_inches='tight', dpi=options.dpi)

def shorten(x, n=48):
    if len(x) > n:
        return x[:n/2] + '..' + x[-n/2:]
    return x

def heatmap_triangle(dataframe, axes, hlabel='Fraction of overlap'):
    """Create a heatmap of the lower triangle of a pairwise correlation
    matrix of all pairs of columns in the given dataframe. The heatmap
    triangle is rotated 45 degrees clockwise and drawn on the given axes.
    Thanks to Kamil Slowikowski for this code https://gist.github.com/slowkow/5797728

    Parameters
    ----------
    dataframe : pandas.DataFrame
    axes : matplotlib.axes.Axes
    """
    N = dataframe.shape[1]
    D = dataframe
    #D = dataframe.corr(method='pearson')

    # UPGMA clustering, but other methods are also available.
    Z = sch.linkage(D, method='average')
    R = sch.dendrogram(Z, no_plot=True)
    cluster_order = R['leaves']
    D = D.ix[cluster_order, cluster_order]

    # Get the lower triangle of the matrix. 
    C = np.tril(D)
    # Mask the upper triangle.
    C = np.ma.masked_array(C, C == 0)
    # Set the diagonal to zero.
    for i in range(N):
        C[i, i] = 0

    # Transformation matrix for rotating the heatmap.
    A = np.array([(y, x) for x in range(N, -1, -1) for y in range(N + 1)])
    t = np.array([[0.5, 1], [0.5, -1]])
    A = np.dot(A, t)

    # -1.0 correlation is blue, 0.0 is white, 1.0 is red.
    # 1.0 correlation is blue, 0.0 is white, 1.0 is red.
    cmap = pl.cm.RdBu_r
    norm = mp.colors.BoundaryNorm(np.linspace(0, 1, 10), cmap.N)

    # This MUST be before the call to pl.pcolormesh() to align properly.
    axes.set_xticks([])
    axes.set_yticks([])

    # Plot the correlation heatmap triangle.
    X = A[:, 1].reshape(N + 1, N + 1)
    Y = A[:, 0].reshape(N + 1, N + 1)
    caxes = pl.pcolormesh(X, Y, np.flipud(C), axes=axes, cmap=cmap, norm=norm)

    # Remove the ticks and reset the x limit.
    axes.set_xlim(right=1)

    # Add a colorbar below the heatmap triangle.
    cb = pl.colorbar(caxes, ax=axes, orientation='horizontal', shrink=0.5825,
                     fraction=0.02, pad=0, ticks=np.linspace(-1, 1, 5),
                     use_gridspec=True)
    cb.set_label(hlabel)

    return caxes, D.index


def pairwise_intersection(options):

    '''
    if options.enrichment:
        FUNC = enrichment_score
        genome_fn = pybedtools.chromsizes_to_file(pybedtools.chromsizes(options.genome))
        kwoptions = dict(genome_fn=genome_fn, iterations=options.iterations,
                processes=options.processes)
    '''

    if options.type == "frac":
        FUNC = frac_of_a
        kwoptions = {}

    elif options.type == 'jaccard':
        FUNC = jaccard_of_a
        kwoptions = {}

    elif options.type == 'fisher':
        FUNC = fisher_of_a
        kwoptions = dict(genome=options.genome)

        #kwoptions = {}

    elif options.type == 'reldist':
        FUNC = reldist_of_a
        kwoptions = {}

    else:
        FUNC = actual_intersection
        kwoptions = {}

    #matrix = create_matrix(beds=options.input, func=FUNC, verbose=options.verbose, **kwoptions)
    matrix, bed_names, bed_sizes = create_matrix(beds=options.input, func=FUNC, verbose=False, sort_bed=options.sort, **kwoptions)


    nfiles = len(options.input)

    output_name =  options.output+'/Intervene_'+options.command+'_'+str(nfiles)+'_files_'

    #if options.verbose:
    #    sys.stderr.write('Time to construct %s x %s matrix: %.1fs' \
    #            % (nfiles, nfiles, (t1 - t0)) + '\n')
    keys = sorted(matrix.keys())
    
    matrix_file = options.output+'/'+str(options.type)+'_pairwise_matrix.txt'
    f = open(matrix_file, 'w')

    #if options.stdout:
    #sys.stdout.write("\t" + "\t".join(keys) + '\n')
    f.write("\t" + "\t".join(keys) + '\n')
    for k in keys:
        #sys.stdout.write(k)
        f.write(k)
        for j in keys:
            #sys.stdout.write('\t' + str(matrix[k][j]))
            f.write('\t' + str(matrix[k][j]))
        #sys.stdout.write('\n')
        f.write('\n')
    f.close()

    if options.htype == 'tribar':
        mp.rc("font", family="serif")
        ncols = nfiles
        matrix = pd.read_table(matrix_file,index_col=0, delim_whitespace=True)

        labels = list(matrix.columns.values)

        series = pd.Series(bed_sizes, index=labels)
        #Set heatmap label
        if options.type == 'count':
            options.hlabel = 'Number of overlap'
        if options.type == 'frac':
            options.hlabel = 'Fraction of overlap'
        if options.type == 'jaccard':
            options.hlabel = 'Jaccard statistic'
        if options.type == 'reldist':
            options.hlabel = 'Relative distance'
        if options.type == 'fisher':
            options.hlabel = 'Fisher p-value'

        #options.title = "Pairwise intersection"
        #options.figsize=(8, 6)

        #series = pd.Series(np.random.random(ncols) * 2.0, index=labels)
        #df = pd.read_csv('data.csv',index_col=0, delim_whitespace=True)
        #matrix = pd.DataFrame(np.random.random((nrows, ncols)), columns=labels)
        outfile = options.output+'/'+str(options.type)+'_barplot_heatmap.'+options.figtype
        barplot(series, matrix, outfile, options, max_size=max(bed_sizes))

        print('\nYou are done! Please check your results @ '+options.output+'. \nThank you for using Intervene!\n')
  
        
    else:
        #print("Please check the matrix file "+matrix_file)
        cmd = 'heatmap_intervene.R %s %s %s %s %s %s %s' % (matrix_file,options.htype,options.type, output_name,options.figtype, str(options.title), options.dpi)
        os.system(cmd)

        print('\nYou are done! Please check your results @ '+options.output+'. \nThank you for using Intervene!\n')



        
