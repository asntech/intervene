#!/usr/bin/env python

## This python wrapper for Vennerable is adopted from - https://github.com/dnlbunting/PyVennerable

import itertools
import rpy2.robjects as ro
import sys
from rpy2.robjects.packages import importr
import os
import tempfile
from intervene import utils


def create_r_script(weights, labels, options, venn_kwargs = {}, plot_kwargs = {"doWeights":"TRUE", 
    "show":'list(Universe = FALSE)'}):
    '''
    It creates Rscript for Vennerable plot for the genomic regions.
    
    Arguments:
        weights (dict):  weights sets to make in to a Venn diagram
        labels (list): List of names of the sets
        venn_kwargs (dict): Dict of args passed directly to Vennerable.Venn()
        plot_kwargs (dict): Dict of args passed directly to plot()
    Returns:
        script_file (str): Rscript file
    '''
    
    if options.scriptonly == False:
        try:
            Vennerable = importr('Vennerable')
        except RRuntimeError:
            print("Unable to load Vennerable in R, make sure it's properly installed or set scriptonly")
            sys.exit(1)

    #temp_f = tempfile.NamedTemporaryFile(delete=False)
    #temp_f = open(tempfile.mktemp(), "w")
    script_file =  options.output+'/'+str(options.project)+'_'+options.command+'.R'
    temp_f = open(script_file, 'w')
    output_name = options.output+'/'+str(options.project)+'_'+options.command+'.'+options.figtype

    temp_f.write('#!/usr/bin/env Rscript'+"\n")
    temp_f.write('if (suppressMessages(!require("Vennerable"))) suppressMessages(remotes::install_github("jenzopr/Vennerable"))\n')
    temp_f.write('library("Vennerable")\n')
    if options.figtype == 'ps':
        temp_f.write('if (suppressMessages(!require("Cairo"))) suppressMessages(install.packages("Cairo", repos="http://cran.us.r-project.org"))\n')
        temp_f.write('library("Cairo")\n')
    
    if options.figtype == 'pdf' or options.figtype == 'svg':
        temp_f.write(options.figtype+'("'+output_name+'", width='+str(options.figsize[0])+', height='+str(options.figsize[1])+', onefile=FALSE, useDingbats=FALSE)'+'\n')
    
    elif options.figtype == 'ps':
        temp_f.write('cairo_ps("'+output_name+'", width='+str(options.figsize[0])+', height='+str(options.figsize[1])+')'+'\n')
    else:
        temp_f.write(options.figtype+'("'+output_name+'", width='+str(options.dpi*options.figsize[0])+', height='+str(options.dpi*options.figsize[1])+', res='+str(options.dpi)+')\n')
     
    weight_string = "c(" + ", ".join(["\'" + k + "\'=" + str(v) for k,v in weights.items() ]) + ")"
    
    venn_type = utils.get_venn_plot_type(options.style, len(labels))

    plot_kwargs = {
    "type": venn_type,
    "doWeights": str(options.weighted).upper(), 
    "show": "list(Universe=FALSE, Faces="+str(options.faces).upper()+")"
    }

    ven_kw = ", ".join([k + " = " + v for k,v in venn_kwargs.items()])    
    plot_kw = ", ".join([k + " = " + v for k,v in plot_kwargs.items()])    
    labels  = "c(\'" + "\', \'".join(labels) + "\')"

    temp_f.write("plot(Venn(" + "Weight = " + weight_string + ", SetNames = " + labels + ", " + ven_kw + ")," + plot_kw +  ")")
    temp_f.write("\n")
    temp_f.write('invisible(dev.off())\n')

    cmd = temp_f.name
    temp_f.close()

    if options.scriptonly == False:
        os.system('chmod +x '+cmd)
        os.system(cmd)
        print('\nSuccessfully completed! Please check your results @ '+options.output+'. \nThank you for using Intervene!\n')
        sys.exit(0)
    else:
        print('\nSuccessfully completed! Please check your UpSet plot script and Shiny App input @ '+options.output+'. \nThank you for using Intervene!\n')
        sys.exit(0)
    return script_file


