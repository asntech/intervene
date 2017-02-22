#!/usr/bin/env python

"""
This is a setup script for Intervene: a toolfor intersection and visualization of multiple genomic region sets

This code is free software; you can redistribute it and/or modify it under the terms of the 
BSD License (see the file LICENSE.md included with the distribution).

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
    'Programming Language :: Python',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.3',
    'Topic :: Scientific/Engineering :: Bio-Informatics',
    'Topic :: Software Development :: Libraries :: Python Modules',
]

install_requires = [
    'pybedtools',
    'matplotlib',
    'pandas',
    'numpy',
    'scipy',
]

#def readme():
#    with open('README.rst') as f:
#        return f.read()

def readme(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="intervene",
    description="A tool for intersection and visualization of multiple gene or genomic region sets",
    version=VERSION,
    author="Aziz Khan",
    license='MIT',
    platforms='linux/unix',
    author_email="azez.khan@gmail.com",
    url="https://github.com/asntech/intervene",
    long_description=readme("README.rst"),
    package_dir={'intervene': 'intervene'},

    packages=['intervene',
        'intervene.modules',
        'intervene.modules.pairwise',
        'intervene.modules.venn',
        'intervene.modules.upset',
        'intervene.example_data',
        'intervene.example_data.dbSUPER_mm9',
        'intervene.example_data.ENCODE_hESC',
        'intervene.example_data.Gene_list'],

    scripts=['intervene/intervene',
                   ],
    package_data={'intervene': ['example_data/dbSUPER_mm9/*.bed', 'example_data/ENCODE_hESC/*.bed','example_data/Gene_list/*.txt',]},
    #package_data={'intervene': ['example_data/*']},
    include_package_data=True,
    install_requires = install_requires,
    classifiers=CLASSIFIERS,


)
