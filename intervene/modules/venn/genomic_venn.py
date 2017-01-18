# coding: utf-8

"""
InterVene: a tool for intersection and visualization of multiple genomic region sets
Created on January 10, 2017
Version: 1.0
@author: <Aziz Khan>aziz.khan@ncmm.uio.no
"""
import sys
import os
from pybedtools import BedTool, example_bedtool
from intervene.modules.venn import list_venn
from intervene.modules.upset import upset


def venn2(a,b,names=['A','B'],plot_type=None, **options):

    a = BedTool(a)
    b = BedTool(b)

    dpi = options.get('dpi', 300)
    output = options.get('output')
    fig_type = options.get('fig_type', 'pdf')

    labels = {'10': (a - b).count(), #Only A
     '01': (b - a).count(), #Only B
     '11': (a + b).count()
     } #Common in A and B

    if plot_type == 'upset':
        upset.draw_genomic(labels, names, output, fig_type)
    
    else:
        fig, ax = list_venn.venn2(labels, names=names, dpi=dpi)

        return fig, ax

def venn3(a,b,c,names=['A','B','C'],plot_type=None, **options):

    a = BedTool(a)
    b = BedTool(b)
    c = BedTool(c)

    dpi = options.get('dpi', 300)
    output = options.get('output')
    fig_type = options.get('fig_type', 'pdf')


    labels = {'001': (c - a - b).count(),
    '010': (b - a - c).count(),
    '011': (b + c - a).count(),
    '100': (a - b - c).count(),
    '101': (a + c - b).count(),
    '110': (a + b - c).count(),
    '111': (a + b + c).count()}

    if plot_type == 'upset':
        upset.draw_genomic(labels, names, output, fig_type)
        
    else:
        fig, ax = list_venn.venn5(labels, names=names, dpi=dpi)
        return fig, ax


def venn4(a,b,c,d, names=['A','B','C','D'],plot_type=None,**options):

    a = BedTool(a)
    b = BedTool(b)
    c = BedTool(c)
    d = BedTool(d)

    dpi = options.get('dpi', 300)
    output = options.get('output')
    fig_type = options.get('fig_type', 'pdf')

    #ABCD
    labels = {'0001': str((d - a - b - c).count()),
    '0010': str((c - a - b - d).count()),
    '0011': str((d + c - b - a).count()),
    '0100': str((b - a - d - c).count()),
    '0101': str((b + d - a - c).count()),
    '0110': str((b + c - a - d).count()),
    '0111': str((d + b + c - a).count()),
    '1000': str((a - b - c - d).count()),
    '1001': str((a + d - b - c).count()),
    '1010': str((a + c - b - d).count()),
    '1011': str((a + c + d - b).count()),
    '1100': str((a + b - c - d).count()),
    '1101': str((a + b + d - c).count()),
    '1110': str((a + b + c - d).count()),
    '1111': str((a + b + c + d).count())
    }
    
    if plot_type == 'upset':
        upset.draw_genomic(labels, names, output, fig_type)
 
    else:
        fig, ax = list_venn.venn4(labels, names=names, dpi=dpi)

        return fig, ax

def venn5(a, b, c, d, e, names=['A','B','C','D','E'], plot_type='venn', **options):

    a = BedTool(a)
    b = BedTool(b)
    c = BedTool(c)
    d = BedTool(d)
    e = BedTool(e)

    dpi = options.get('dpi', 300)
    output = options.get('output')
    fig_type = options.get('fig_type', 'pdf')

    #ABCDE
    labels = {'00001': (e - a - b - c - d).count(),
    '00010': str((d - a - b - c - e).count()),
    '00011': str((d + e - a - b - c).count()),
    '00100': str((c - a - b - d - e).count()),
    '00101': str((c + e - a - b - d).count()),
    '00110': str((c + d - a - b - e).count()),
    '00111': str((c + d + e- a - b).count()),
    '01000': str((b - a - c - d - e).count()),
    '01001': str((b + e - a - c - d).count()),
    '01010': str((b + d - a - c - e).count()),
    '01011': str((b + d + e - a - c).count()),
    '01100': str((b + c - a - d - e).count()),
    '01101': str((b + c + e - a - d).count()),
    '01110': str((b + c + d - a - e).count()),
    '01111': str((b + c + d + e - a).count()),
    '10000': str((a - b - c - d - e).count()),
    '10001': str((a + e - b - c - d).count()),
    '10010': str((a + d - b - c - e).count()),
    '10011': str((a + d + e - b - c).count()),
    '10100': str((a + c - b - d - e).count()),
    '10101': str((a + c + e - b - d).count()),
    '10110': str((a + c + d - b - e).count()),
    '10111': str((a + c + d + e - b).count()),
    '11000': str((a + b - c - d - e).count()),
    '11001': str((a + b + e - c - d).count()),
    '11010': str((a + b + d - c - e).count()),
    '11011': str((a + b + d + e - c).count()),
    '11100': str((a + b + c - d - e).count()),
    '11101': str((a + b + c + e - d).count()),
    '11110': str((a + b + c + d - e).count()),
    '11111': str((a + b + c + d + e).count())
    }
    
    if plot_type == 'upset':
        #upset.draw_genomic(labels, names, output, fig_type)
        upset.create_r_script(labels, names, output, fig_type)


    else:
        fig, ax = list_venn.venn5(labels, names=names, dpi=dpi)
        return fig, ax


def venn6(a,b,c,d,e,f,names=['A','B','C','D','E','F'],plot_type=None, **options):
    """
    6-way Venn diagram from a list of six genomic region sets in <BED/GTF/GFF/VCF> format.

    """

    a = BedTool(a)
    b = BedTool(b)
    c = BedTool(c)
    d = BedTool(d)
    e = BedTool(e)
    f = BedTool(f)

    dpi = options.get('dpi', 300)
    output = options.get('output')
    fig_type = options.get('fig_type', 'pdf')

    #ABCDEF
    labels = {'000001': str((f - a - b - c - d - e).count()),
    '000010': str((e - a - b - c - d - f).count()),
    '000011': str((e + f - a - b - c - d).count()),
    '000100': str((d - a - b - c - e - f).count()),
    '000101': str((d + f - a - b - c - e).count()),
    '000110': str((d + e - a - b - c - f).count()),
    '000111': str((d - e - f - a - b - c).count()),
    '001000': str((c - a - b - d - e - f).count()),
    '001001': str((c + f - a - b - d - e).count()),
    '001010': str((c + e - a - b - d - f).count()),
    '001011': str((c + e + f - a - b - d).count()),
    '001100': str((- a - b - c - d - e - f).count()),
    '001101': str((- a - b - c - d - e - f).count()),
    '001110': str((- a - b - c - d - e - f).count()),
    '001111': str((- a - b - c - d - e - f).count()),
    '010000': str((- a - b - c - d - e - f).count()),
    '010001': str((- a - b - c - d - e - f).count()),
    '010010': str((- a - b - c - d - e - f).count()),
    '010011': str((- a - b - c - d - e - f).count()),
    '010100': str((- a - b - c - d - e - f).count()),
    '010101': str((- a - b - c - d - e - f).count()),
    '010110': str((- a - b - c - d - e - f).count()),
    '010111': str((- a - b - c - d - e - f).count()),
    '011000': str((- a - b - c - d - e - f).count()),
    '011001': str((- a - b - c - d - e - f).count()),
    '011010': str((- a - b - c - d - e - f).count()),
    '011011': str((- a - b - c - d - e - f).count()),
    '011100': str((- a - b - c - d - e - f).count()),
    '011101': str((- a - b - c - d - e - f).count()),
    '011110': str((- a - b - c - d - e - f).count()),
    '011111': str((- a - b - c - d - e - f).count()),
    '100000': str((- a - b - c - d - e - f).count()),
    '100001': str((- a - b - c - d - e - f).count()),
    '100010': str((- a - b - c - d - e - f).count()),
    '100011': str((- a - b - c - d - e - f).count()),
    '100100': str((- a - b - c - d - e - f).count()),
    '100101': str((- a - b - c - d - e - f).count()),
    '100110': str((- a - b - c - d - e - f).count()),
    '100111': str((- a - b - c - d - e - f).count()),
    '101000': str((- a - b - c - d - e - f).count()),
    '101001': str((- a - b - c - d - e - f).count()),
    '101010': str((- a - b - c - d - e - f).count()),
    '101011': str((- a - b - c - d - e - f).count()),
    '101100': str((- a - b - c - d - e - f).count()),
    '101101': str((- a - b - c - d - e - f).count()),
    '101110': str((- a - b - c - d - e - f).count()),
    '101111': str((a + c + d + e + f - b).count()),
    '110000': str((- a - b - c - d - e - f).count()),
    '110001': str((- a - b - c - d - e - f).count()),
    '110010': str((- a - b - c - d - e - f).count()),
    '110011': str((- a - b - c - d - e - f).count()),
    '110100': str((a + b + d - c - e - f).count()),
    '110101': str((a + b + d + f + e - c).count()),
    '110110': str((a + b + d + e - f - c).count()),
    '110111': str((a + b + d + e + f - c).count()),
    '111000': str((a + b + c - d - e - f).count()),
    '111001': str((a + b + c + f - d - e).count()),
    '111010': str((a + b + c + e - d - f).count()),
    '111011': str((a + b + c + e + f - d).count()),
    '111100': str((a + b + c + d - e - f).count()),
    '111101': str((a + b + c + d + f - e).count()),
    '111110': str((a + b + c + d + e - f).count()),
    '111111': str((a + b + c + d + e + f).count())
    }

    if plot_type == 'upset':
        upset.write_r_script(labels, names, output,fig_type)

    else:
        fig, ax = list_venn.venn5(labels, names=names, dpi=dpi)
        
        return fig, ax
