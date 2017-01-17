#!/usr/bin/env python

"""
This is a setup script for InterVene: a toolfor intersection and visualization of multiple genomic region sets

This code is free software; you can redistribute it and/or modify it under the terms of the 
BSD License (see the file LICENSE.md included with the distribution).

@version: 0.1
@author: Aziz Khan
@email: aziz.khan@ncmm.uio.no
"""
import os
from distutils.core import setup
from setuptools import find_packages

from intervene import __version__ as VERSION


CLASSIFIERS = [
    'Intended Audience :: Developers',
    'Intended Audience :: Science/Research',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 2.7',
    'Topic :: Scientific/Engineering :: Bio-Informatics',
]

install_requires = [
    'pybedtools',
    'argparse'
]

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="intervene",
    description="A tool for intersection and visualization of multiple genomic region sets",
    version=VERSION,
    author="Aziz Khan",
    license='MIT',
    platforms='linux/unix',
    Keywords= "bioinformatics genomics",
    author_email="azez.khan@gmail.com",
    url="https://github.com/asntech/intervene",
    #long_description=read('README.md'),
    package_dir={'intervene': 'intervene'},

    packages=['intervene', 'intervene.modules','intervene.modules.pairwise',
    'intervene.modules.venn','intervene.modules.upset'],

    scripts=['intervene/intervene','intervene/scripts/intervene_upset_plot.R','intervene/scripts/intervene_heatmap.R',
                   ],
    package_data={'intervene': ['intervene/example_data/*.*']},
    include_package_data=True,
    install_requires = install_requires,
    classifiers=CLASSIFIERS,
)
