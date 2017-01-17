# coding: utf-8

"""
InterVene: a tool for intersection and visualization of multiple genomic region sets
Created on January 10, 2017
Version: 1.0
@author: <Aziz Khan>aziz.khan@ncmm.uio.no
"""
import os
import sys
import collections
import time
import os.path as op
import pybedtools
from pybedtools import BedTool, example_filename


def get_name(fname):
    return op.splitext(op.basename(fname))[0]


def actual_intersection(a, b):
    return len(a.intersect(b, u=True))

def jaccard_of_a(a, b):
    return a.jaccard(b,u=True)['jaccard']

#Calculate the fisher 
def fisher_of_a(a, b):
    return a.fisher(b,genome='hg19').two_tail

#Calculate the reldist 
def reldist_of_a(a, b):
    #return mean(a.reldist(b)['reldist'])
    return float(sum(a.reldist(b)['reldist'])) / max(len(a.reldist(b)['reldist']), 1)

def frac_of_a(a, b):
    len_a = float(len(a))
    return len(a.intersect(b, u=True)) / len_a

def enrichment_score(a, b, genome_fn, iterations=None, processes=None):
    results = a\
            .randomstats(b, new=True, genome_fn=genome_fn, iterations=iterations, processes=processes)
    return (results['actual'] + 1) / (results['median randomized'] + 1)

def create_matrix(beds, func, verbose=False, **kwoptions):
    nfiles = len(beds)
    total = nfiles ** 2
    i = 0
    bed_sizes = []
    bed_names = []

    matrix = collections.defaultdict(dict)
    for fa in beds:
        a = BedTool(fa)
        for fb in beds:
            i += 1
            b = BedTool(fb)

            if verbose:
                sys.stderr.write(
                        '%(i)s of %(total)s: %(fa)s + %(fb)s\n' % locals())
                sys.stderr.flush()

            matrix[get_name(fa)][get_name(fb)] = func(a, b, **kwoptions)

        bed_names.append(get_name(fa))
        bed_sizes.append(len(a))
    return matrix, bed_names,bed_sizes

def pairwise_intersection(options):
    if options.test:
    # insulator binding sites from ChIP-chip -- 4 proteins, 2 cell types
    # Genes Dev. 2009 23(11):1338-1350
        options.input = [example_filename(i) for i in  [
                'Cp190_Kc_Bushey_2009.bed',
                'Cp190_Mbn2_Bushey_2009.bed',
                'CTCF_Kc_Bushey_2009.bed',
                'CTCF_Mbn2_Bushey_2009.bed',
                'SuHw_Kc_Bushey_2009.bed',
                'SuHw_Mbn2_Bushey_2009.bed',
                'BEAF_Mbn2_Bushey_2009.bed',
                'BEAF_Kc_Bushey_2009.bed'
                ]]

    if options.enrichment:
        FUNC = enrichment_score
        genome_fn = pybedtools.chromsizes_to_file(pybedtools.chromsizes(options.genome))
        kwoptions = dict(genome_fn=genome_fn, iterations=options.iterations,
                processes=options.processes)

    elif options.type == "frac":
        FUNC = frac_of_a
        kwoptions = {}

    elif options.type == 'jaccard':
        FUNC = jaccard_of_a
        kwoptions = {}

    elif options.type == 'fisher':
        FUNC = fisher_of_a
        kwoptions = {}

    elif options.type == 'reldist':
        FUNC = reldist_of_a
        kwoptions = {}

    else:
        FUNC = actual_intersection
        kwoptions = {}

    t0 = time.time()
    #matrix = create_matrix(beds=options.input, func=FUNC, verbose=options.verbose, **kwoptions)
    matrix, bed_names, bed_sizes = create_matrix(beds=options.input, func=FUNC, verbose=False, **kwoptions)

    #print(bed_sizes)

    t1 = time.time()

    nfiles = len(options.input)

    output_name =  options.output+'/InterVene_'+options.command+'_'+str(nfiles)+'_files_'

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
    #print("Please check the matrix file "+matrix_file)
    cmd = 'intervene_heatmap.R %s %s %s %s %s' % (matrix_file,options.htype,options.type, output_name,options.figtype)
    os.system(cmd)

    print('\nYou are done! Please check your results @ '+options.output+'. \nThank you for using InterVene!\n')


