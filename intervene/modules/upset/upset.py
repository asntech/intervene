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

def create_r_script(labels, names, output, fig_type):
    #temp_f = tempfile.NamedTemporaryFile(delete=False)
    #temp_f = open(tempfile.mktemp(), "w")
    script_file = output+'/'+'intervene_upset_plot.R'
    temp_f = open(script_file, 'w')
    output_name = output+'/'+'intervene_upset_plot.pdf'

    temp_f.write('#!/usr/bin/env Rscript'+"\n")
    temp_f.write('library("UpSetR")\n')
    temp_f.write('pdf("'+output_name+'", width=8, height=5)\n')
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

    temp_f.write('upset(fromExpression(expressionInput), nsets='+str(len(key))+', main.bar.color="brown",sets.bar.color="#56B4E9", order.by = "freq", number.angles = 45, mainbar.y.label = "No of Intersections", sets.x.label = "Number of ChIP-seq peaks")\n')
    temp_f.write('invisible(dev.off())\n')

    #print temp_f.read()
    #print temp_f.name
    #cmd = 'intervene_upset_plot.R %s %s %s' % ('genomic',5,temp_f.name)
    cmd = temp_f.name
    temp_f.close()
    os.system('chmod +x '+cmd)
    os.system(cmd)
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
    cmd = 'intervene_upset_plot.R %s %s %s %s %s ' % ('genomic',len(key),temp_f.name, output, fig_type)
    os.system(cmd)
    sys.exit(1)
    