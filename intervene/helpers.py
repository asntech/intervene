# coding: utf-8
'''
Helper functions for Intervene
'''
import sys
import os
import intervene
from matplotlib import colors

def create_dir(dir_path):
    '''
    Create a output directory if it's not exists.
    '''

    if not os.path.exists(dir_path):
        try:
            os.makedirs(dir_path)
        except:
            sys.exit( "Output directory (%s) could not be created." % dir_path )
    return dir_path

def venn_order(input_files):
    """
    Checks the order of venn plot. 

    @type input_files: list[Iterable] 
    @rtype int 

    input
      input_files: a list of files of genomic regions or lists

    return
      len(input_files): return length of input files
    """

    return len(input_files)

def get_filenames(input_files):
    """
    Checks the venn-type

    @type input_files: list[Iterable] 
    @rtype file_names: list[Iterable]

    input
      input_files: a list of files of genomic regions or lists

    return
      file_names:: return a list of file names
    """
    file_names=[]
    for fname in input_files:
      file_names.append(os.path.splitext(os.path.basename(fname))[0])

    return file_names

"""
Provides access to example files

"""

def data_dir():
    """
    Returns the data directory that contains example files.
    """
    #data_path = os.path.dirname(intervene.__file__)
    #data_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'example_data')
    #print(data_path)
    return os.path.join(os.path.dirname(__file__), 'example_data')


def example_filename(fn,sub_dir=None):
    """
    Return a bed file from the pybedtools examples directory.
    This code is adapted from https://github.com/daler/pybedtools

    """
    #print(data_dir())
    #sys.exit()
    if sub_dir:
      fn = os.path.join(data_dir(), sub_dir, fn)
    else:
      fn = os.path.join(data_dir(), fn)
    #print(fn)
    if not os.path.exists(fn):
        raise ValueError("%s does not exist" % fn)
    return fn

def get_test_data(module_name):
  '''
  It returns a list of test data files, if the user uses --test argument
  
  @type module_name: chr
  @rtype test_files: list[Iterable]

  input
      module_name: Name of Intervene module

  return
      test_files:: return a list of file paths

  '''

  test_files = []
  
  if module_name == 'venn':
    test_files = [example_filename(i,'ENCODE_hESC') for i in  [
        'H3K27ac.bed',
        #'H3K4me2.bed',
        'H3K4me3.bed',
        'H3K27me3.bed'
        ]]

  elif module_name == 'upset':
    test_files = [example_filename(i, 'ENCODE_hESC') for i in  [
        'H3K27ac.bed',
        #'H3K4me2.bed',
        #'H3K4me1.bed',
        'H3K4me3.bed',
        'H3K27me3.bed'
        ]]

  elif module_name == 'pairwise':
    test_files = [example_filename(i, 'dbSUPER_mm9') for i in  [
        'Bone_Marrow.bed',
        'Cerebellum.bed',
        'Cortex.bed',
        'E14.5_Brain.bed',
        'E14.5_Heart.bed',
        'E14.5_Limb.bed',
        'E14.5_Liver.bed',
        'Heart.bed',
        'HFSCs.bed',
        'Intestine.bed',
        'Kidney.bed',
        'Liver.bed',
        'Lung.bed',
        'Macrophage.bed',
        'MEF.bed',
        'mESC.bed',
        'Myotubes.bed',
        'Olfactory_Bulb.bed',
        'pro-B.bed',
        'Spleen.bed',
        'TACs.bed',
        'Testis.bed',
        'Th_Cells.bed',
        'Thymus.bed'
        ]]
  else:
    sys.exit(1)

  return test_files

def default_colors():
    """
    Get a list of RGBA colors 
    """
    # default_colors = [
    #     # r, g, b, a
    #     [92, 192, 98, 0.5],
    #     [90, 155, 212, 0.5],
    #     [246, 236, 86, 0.6],
    #     [241, 90, 96, 0.4],
    #     [255, 117, 0, 0.3],
    #     [82, 82, 190, 0.2],
    # ]

    default_colors = [
        # r, g, b, a
        [188, 114, 3, 0.5],
        [3, 133, 188, 0.5],
        [155, 9, 118, 0.6],
        [155, 53, 9, 0.4],
        [4, 140, 128, 0.3],
        [140, 8, 8, 0.2],
    ]

    default_colors = [
        [i[0] / 255.0, i[1] / 255.0, i[2] / 255.0, i[3]]
        for i in default_colors
    ]

    return default_colors

def get_colors(color_list):
    """
    Get color combinations for Venn diagram. This converts color names to RGBA 

    """
    rgba_colors = []
    a = [0.5,0.5,0.6,0.4,0.3,0.2]
    i = 0
    for c in color_list:
        rgba_colors.append(list(colors.to_rgba(c)))
        rgba_colors[i][3] = a[i]
        i+=1

    return rgba_colors
