# coding: utf-8

"""
InterVene: a tool for intersection and visualization of multiple genomic region sets
Created on January 10, 2017
@author: <Aziz Khan>aziz.khan@ncmm.uio.no
"""
import sys
import os
import tempfile
import itertools
from intervene.modules.pairwise.pairwise import get_name
from pybedtools import BedTool, helpers


def genomic_upset(input_files):
    '''
    Arguments:
        input_files -  List of BED files to to calculate the weights
    Takes a list of sets a list of the sizes of non-overlapping intersections between them 
    '''
    
    N = len(input_files)
    
    # Generate a truth table of intersections to calculate 
    truth_table = [x for x in itertools.product("01", repeat=N)][1:]

    weights = {}

    for t in truth_table:
        ones = [BedTool(input_files[i]) for i in range(N) if t[i] =='1']
        zeros = [BedTool(input_files[i]) for i in range(N) if t[i] =='0']
        
        #report those entries in set A which do ovelap with other sets
        x = ones[0]
        if len(ones) > 1:
            for bed in ones[1:]:
                x = x.intersect(bed, u=True)

        #report those entries in set A which doesn't ovelap with other sets
        if len(zeros) > 0:
            #y = zeros[0]
            for bed in zeros[0:]:
                x = x.intersect(bed, v=True)
        
        X = (x).count() 

        weights[''.join(t)] = X

    #delete all temp files
    helpers.cleanup()
    
    return(weights)

def list_upset(input_files):
    '''
    Arguments:
        input_files -  List of list files to calculate weights for upset plot
    Takes a list of sets a list of the sizes of non-overlapping intersections between them 
    '''
    S =[]
    for f in input_files:
        a = open(f, 'r').read().splitlines()
        S.append(set(a))

    N = len(S)
    
    # Generate a truth table of intersections to calculate 
    truth_table = [x for x in itertools.product("01", repeat=N)][1:]

    
    weights = {}
    for t in truth_table:
        ones = [S[i] for i in range(N) if t[i] =='1']
        zeros = [S[i] for i in range(N) if t[i] =='0']
        
        X = set.intersection(*ones)
        X.difference_update(*zeros)
        
        weights[''.join(t)] = len(X)
    
    return(weights)

def create_r_script(labels, names, options):
    """
    It create Rscript for UpSetR plot for the genomic regions.

    """
    #temp_f = tempfile.NamedTemporaryFile(delete=False)
    #temp_f = open(tempfile.mktemp(), "w")
    script_file =  options.output+'/'+str(options.project)+'_'+options.command+'.R'
    temp_f = open(script_file, 'w')
    output_name = options.output+'/'+str(options.project)+'_'+options.command+'.'+options.figtype

    temp_f.write('#!/usr/bin/env Rscript'+"\n")
    temp_f.write('if (suppressMessages(!require("UpSetR"))) suppressMessages(install.packages("UpSetR", repos="http://cran.us.r-project.org"))\n')
    temp_f.write('library("UpSetR")\n')
    if options.figtype == 'ps':
        temp_f.write('if (suppressMessages(!require("Cairo"))) suppressMessages(install.packages("Cairo", repos="http://cran.us.r-project.org"))\n')
        temp_f.write('library("Cairo")\n')
    
    if options.figtype == 'pdf' or options.figtype == 'svg':
        temp_f.write(options.figtype+'("'+output_name+'", width='+str(options.figsize[0])+', height='+str(options.figsize[1])+', onefile=FALSE)'+'\n')
    
    elif options.figtype == 'ps':
        temp_f.write('cairo_ps("'+output_name+'", width='+str(options.figsize[0])+', height='+str(options.figsize[1])+')'+'\n')
    else:
        temp_f.write(options.figtype+'("'+output_name+'", width='+str(options.dpi*options.figsize[0])+', height='+str(options.dpi*options.figsize[1])+', res='+str(options.dpi)+')\n')
     
    temp_f.write("expressionInput <- c(")

    last = 1

    shiny = ""

    for key, value in labels.items(): #iteritems in python 2.7
        i = 0
        first = 1
        for x in key:
            if i == 0:
                temp_f.write("'")
      
            if x == '1':
                if first == 1:
                    temp_f.write(str(names[i]))
                    shiny += str(names[i])
                    first = 0
                else:
                    temp_f.write('&'+str(names[i]))
                    shiny += '&'+str(names[i])

            if i == len(key)-1:
                if last == len(labels):
                    temp_f.write("'="+str(value))
                    shiny += "="+str(value)

                else:
                    temp_f.write("'="+str(value)+',')
                    shiny += "="+str(value)+','
            i += 1
        last +=1
    temp_f.write(")\n")

    #options.shiny = True
    #If shiny output
    if options.showshiny == False:

        shiny_import =  options.output+'/'+str(options.project)+'_'+options.command+'_combinations.txt'
        shiny_file = open(shiny_import, 'w')
        shiny_file.write("You can go to Intervene Shiny App https://asntech.shinyapps.io/Intervene-app/ and copy/paste the following intersection data to get more interactive figures.\n\n")
        shiny_file.write(shiny)
        shiny_file.close()
    
    else:
        print(shiny)

    if options.showsize:
        options.showsize = 'yes'

    #if options.ninter == 0:
    #    options.ninter = "NA"

    if options.showzero == False:
        options.showzero = 'NULL'
    else:
        options.showzero = "'on'"

    temp_f.write('upset(fromExpression(expressionInput), nsets='+str(len(key))+', nintersects='+str(options.ninter)+', show.numbers="'+str(options.showsize)+'", main.bar.color="'+options.mbcolor+'", sets.bar.color="'+options.sbcolor+'", empty.intersections='+str(options.showzero)+', order.by = "'+options.order+'", number.angles = 0, mainbar.y.label ="'+options.mblabel+'", sets.x.label ="'+options.sxlabel+'")\n')
    temp_f.write('invisible(dev.off())\n')

    #print temp_f.read()
    #print temp_f.name
    #cmd = 'intervene_upset_plot.R %s %s %s' % ('genomic',5,temp_f.name)
    cmd = temp_f.name
    temp_f.close()

    if options.scriptonly == False:
        os.system('chmod +x '+cmd)
        os.system(cmd)
        print('\nYou are done! Please check your results @ '+options.output+'. \nThank you for using Intervene!\n')
        sys.exit(0)
    else:
        print('\nYou are done! Please check your UpSet plot script and Shiny App input @ '+options.output+'. \nThank you for using Intervene!\n')
        sys.exit(0)

        
def draw_genomic(labels, names, output, fig_type):
    #temp_f = tempfile.NamedTemporaryFile(delete=False)
    temp_f = open(tempfile.mktemp(), "w")
    
    temp_f.write("expressionInput <- c(")
    last = 1
    for key, value in labels.items():
        i = 0
        first = 1
        for x in key:
            if i == 0:
                #print("'")
                temp_f.write("'")      
            if x == '1':
                if first == 1:
                    temp_f.write(str(names[i]))
                    #print(str(names[i]))
                    first = 0
                else:
                    temp_f.write('&'+str(names[i]))
                    #print('&'+str(names[i]))

            if i == len(key)-1:
                if last == len(labels):
                    temp_f.write("'="+str(value))
                else:
                    temp_f.write("'="+str(value)+',')
                #print("'="+str(value)+',')
            i += 1
        last +=1
        #print("'="+str(value)+',')
        #temp_f.write("'="+str(value)+',')
    temp_f.write(")\n")
    #print temp_f.read()
    #print temp_f.name
    temp_f.close()
    cmd = 'upset_plot_intervene.R %s %s %s %s %s ' % ('genomic',len(key),temp_f.name, output, fig_type)
    os.system(cmd)
    sys.exit(1)


def one_vs_rest_intersection(beds, peaks, output, **kwoptions):
    '''
    Compares a set of peaks with several other peaks sets.

    '''
    names = []
    matrix_file = output+'/One_vs_all_peak_set_matrix.txt'
    f = open(matrix_file, 'w')
    
    f.write('peak_id')
    #f.write('peak_id\tchrom\tstart\tend')

    for bed in beds:
        names.append(get_name(bed))
        f.write('\t' + str(get_name(bed)))
    #main_int.append(names)

    peaks = BedTool(peaks[0])
    f.write('\n')
    for i in peaks:
        #region_int = []
        peak_id = str(i.chrom)+"_"+str(i.start)+"_"+str(i.end)
        f.write(peak_id)
        #f.write(peak_id + '\t' + i.chrom + '\t' + str(i.start) + '\t' + str(i.end))

        for bed in beds:
            b = BedTool(bed)
            int_count = BedTool(str(i), from_string=True).intersect(b).count()
            if (int_count > 0):
                #region_int.append("1")
                f.write('\t' + str(1))
            else:
                #region_int.append("0")
                f.write('\t' + str(0))
        f.write('\n')
        #main_int.append(region_int)
        #matrix[peak_id] = region_int
    f.close()

    return matrix_file
    