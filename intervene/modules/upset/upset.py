# coding: utf-8

"""
InterVene: a tool for intersection and visualization of multiple genomic region sets
Created on January 10, 2017
Version: 1.0
@author: <Aziz Khan>aziz.khan@ncmm.uio.no
"""
import sys
import os
import tempfile

def create_r_script(labels, names, options):
    """
    It create an Rscript for UpSetR plot for the genomic regions.


    """
    #temp_f = tempfile.NamedTemporaryFile(delete=False)
    #temp_f = open(tempfile.mktemp(), "w")
    script_file = options.output+'/'+'intervene_'+options.type+'_UpSet_plot.R'
    temp_f = open(script_file, 'w')

    output_name = options.output+'/'+'intervene_'+options.type+'_UpSet_plot.'+options.figtype

    temp_f.write('#!/usr/bin/env Rscript'+"\n")
    temp_f.write('library("UpSetR")\n')
    
    if options.figtype == 'pdf':
        temp_f.write(options.figtype+'("'+output_name+'", width=8, height=5)'+'\n')
    else:
        temp_f.write(options.figtype+'("'+output_name+'", width=8, height=5, res='+str(options.dpi)+')\n')
    
    temp_f.write("expressionInput <- c(")

    last = 1
    for key, value in labels.iteritems():
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

    if options.showsize:
        options.showsize = 'yes'

    #if options.ninter == 0:
    #    options.ninter = "NA"

    if not options.showzero:
        options.showzero = 'NULL'
    else:
        options.showzero = 'on'

    temp_f.write('upset(fromExpression(expressionInput), nsets='+str(len(key))+', nintersects='+str(options.ninter)+', show.numbers="'+str(options.showsize)+'", main.bar.color="'+options.mbcolor+'", sets.bar.color="'+options.sbcolor+'", empty.intersections="'+str(options.showzero)+'", order.by = "'+options.order+'", number.angles = 0, mainbar.y.label ="'+options.mblabel+'", sets.x.label ="'+options.sxlabel+'")\n')
    temp_f.write('invisible(dev.off())\n')

    #print temp_f.read()
    #print temp_f.name
    #cmd = 'intervene_upset_plot.R %s %s %s' % ('genomic',5,temp_f.name)
    cmd = temp_f.name
    temp_f.close()

    if options.run == True:
        os.system('chmod +x '+cmd)
        os.system(cmd)
        sys.exit(1)
    else:
        print('Please find the Rscript here: '+cmd)
        sys.exit(1)

        
def draw_genomic(labels, names, output, fig_type):
    #temp_f = tempfile.NamedTemporaryFile(delete=False)
    temp_f = open(tempfile.mktemp(), "w")
    
    temp_f.write("expressionInput <- c(")
    last = 1
    for key, value in labels.iteritems():
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
    