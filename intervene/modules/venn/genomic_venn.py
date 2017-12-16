# coding: utf-8

"""
InterVene: a tool for intersection and visualization of multiple genomic region sets
Created on January 10, 2017
@author: <Aziz Khan>aziz.khan@ncmm.uio.no
"""
import sys
import os
from pybedtools import BedTool, helpers
from intervene.modules.venn import list_venn
from intervene.modules.upset import upset


def venn2(input_files, options,names=['A','B'], plot_type='venn'):
    """
    2-way Venn diagram from a list of six genomic region sets in <BED/GTF/GFF/VCF> format.

    """

    labels = upset.genomic_upset(options.input, options.output)

    if plot_type == 'upset':
        upset.create_r_script(labels, names, options)
    
    else:
        fig, ax = list_venn.venn2(labels, names=names, dpi=options.dpi, colors=options.colors, figsize=options.figsize)

        return fig, ax

def venn3(input_files, options, names=['A','B','C'], plot_type='venn'):
    """
    3-way Venn diagram from a list of six genomic region sets in <BED/GTF/GFF/VCF> format.

    """

    labels = upset.genomic_upset(options.input, options.output)

    if plot_type == 'upset':
        upset.create_r_script(labels, names, options)
        
    else:
        fig, ax = list_venn.venn3(labels, names=names, dpi=options.dpi, colors=options.colors,  figsize=options.figsize)
        return fig, ax


def venn4(input_files, options, names=['A','B','C','D'],plot_type='venn'):
    """
    4-way Venn diagram from a list of six genomic region sets in <BED/GTF/GFF/VCF> format.

    """

    labels = upset.genomic_upset(options.input, options.output)
    
    if plot_type == 'upset':
        upset.create_r_script(labels, names, options)
 
    else:
        fig, ax = list_venn.venn4(labels, names=names, dpi=options.dpi, colors=options.colors, figsize=options.figsize)

        return fig, ax

def venn5(input_files, options, names=['A','B','C','D','E'], plot_type='venn'):
    """
    5-way Venn diagram from a list of six genomic region sets in <BED/GTF/GFF/VCF> format.

    """

    labels = upset.genomic_upset(options.input, options.output)
    
    if plot_type == 'upset':
        #upset.draw_genomic(labels, names, output, fig_type, options)
        upset.create_r_script(labels, names, options)

    else:
        fig, ax = list_venn.venn5(labels, names=names, dpi=options.dpi, colors=options.colors, figsize=options.figsize)
        return fig, ax


def venn6(input_files, options, names=['A','B','C','D','E','F'],plot_type='venn'):
    """
    6-way Venn diagram from a list of six genomic region sets in <BED/GTF/GFF/VCF> format.

    """

    labels = upset.genomic_upset(options.input, options.output)

    if plot_type == 'upset':
        upset.create_r_script(labels, names, options)

    else:
        fig, ax = list_venn.venn6(labels, names=names, dpi=options.dpi, colors=options.colors, figsize=options.figsize)
        
        return fig, ax
