.. image:: https://travis-ci.org/asntech/intervene.svg?branch=master
    :target: https://travis-ci.org/asntech/intervene

.. image:: https://badge.fury.io/py/intervene.svg
    :target: https://badge.fury.io/py/intervene

.. image:: https://img.shields.io/github/issues/asntech/intervene.svg
	:target: https://github.com/asntech/intervene/issues

.. image:: https://readthedocs.org/projects/intervene/badge/?version=latest
   :target: https://readthedocs.org/projects/intervene/?badge=latest
   :alt: sphinx documentation for latest release
   
.. image:: https://img.shields.io/twitter/url/https/github.com/asntech/intervene.svg?style=social
	:target: https://twitter.com/intent/tweet?text=Intervene%20-%20a%20tool%20for%20intersection%20and%20visualization%20of%20multiple%20genomic%20region%20and%20gene%20sets%20https://github.com/asntech/intervene&url=%5Bobject%20Object%5D

Introduction
============
Intervene is a tool for intersection and visualization of multiple gene or genomic region sets.

`Read detailed documentation here <http://intervene.readthedocs.org>`_

.. figure:: http://intervene.readthedocs.io/en/latest/_images/Intervene_plots.png
   :width: 800px
   :align: left

Installation
============

Intervene requires the following Python modules and R packages:

	* Python (=> 2.7 ): https://www.python.org/
	* BedTools (Latest version): https://github.com/arq5x/bedtools2
	* pybedtools (>= 0.7.9): https://daler.github.io/pybedtools/
	* Pandas (>= 0.16.0): http://pandas.pydata.org/
	* R (>= 3.0): https://www.r-project.org/
	* R packages including UpSetR, corrplot

Install BEDTools
----------------
We are using pybedtools, which is Python wrapper for BEDTools. So, BEDTools should be installed before using Intervene. It's recomended to have a latest version, but if you have an older version already install, it should be fine.

A quick installation, if you have conda installed.

.. code-block:: bash

    conda install -c bioconda bedtools

Please read the instructions at https://github.com/arq5x/bedtools2 to install BEDTools, and make sure it is on your path and you are able to call bedtools from any directory.

Install required Python modules
-------------------------------
Intervene takes care of the installation of all the required Python modules. If you already have a working installation of Python, the easiest way to install Intervene is by using ``pip``. If you're setting up Python for the first time, we recommend to install it using Anaconda Python distribution http://continuum.io/downloads. These come with several helpful scientific and data processing libraries. These are available for platforms including Windows, Mac OSX and Linux.


Install required R packages
---------------------------

Intervene rquires two R packages, `UpSetR <https://cran.r-project.org/package=UpSetR>`_ , `corrplot <https://cran.r-project.org/package=corrplot>`_ for visualization and `Cairo <https://cran.r-project.org/package=Cairo>`_ to generate high-quality vector and bitmap figures.

.. code-block:: R

    install.packages(c("UpSetR", "corrplot", "Cairo"))

Install Intervene
=================
You can install a stable version of Intervene by using ``pip`` from PyPi or a development version by using ``git`` from GitHub.

Install using `pip`
-------------------
You can install InterVene either from PyPi using pip or install it from the source. Please make sure you have already installed the above mentioned python libraries required to run InterVene.

Install from PyPi::

	pip install intervene

Install development version from `Bitbucket`
--------------------------------------------

If you have `git` installed, use this:

.. code-block:: bash

    git clone https://bitbucket.org/CBGR/intervene.git
    cd intervene
    python setup.py install

Install development version from `GitHub`
-----------------------------------------
If you have `git` installed, use this:

.. code-block:: bash

    git clone https://github.com/asntech/intervene.git
    cd intervene
    python setup.py install

How to use Intervene
====================
Once you have installed Intervene, you can type:

.. code-block:: bash

	intervene --help

	usage: intervene <subcommand> [options]
	    
	positional arguments <subcommand>:
	  {venn,upset,pairwise}
	                        List of subcommands
	    venn                Venn diagram of intersection of genomic regions or list sets (upto 6-way).
	    upset               UpSet diagram of intersection of genomic regions or list sets.
	    pairwise            Pairwise intersection and heatmap of N genomic region sets in <BED/GTF/GFF> format.

	optional arguments:
	  -h, --help            show this help message and exit
	  -v, --version         show program's version number and exit


to see the help for the three subcommands ``pairwise``, ``venn`` and ``upset`` type::

.. code-block:: bash
	
	intervene pairwise --help

	intervene venn --help

	intervene upset --help

Run Intervene on test data
--------------------------

To run Intervene using example data, use the following commands. To access the test data make sure you have ``sudo`` or ``root`` access.

.. code-block:: bash

	intervene pairwise --test

	intervene venn --test

	intervene upset --test

If you have installed Intervene locally from the source code, you may have problem to find test data. You can download the test data here https://github.com/asntech/intervene/tree/master/intervene/example_data and point to it using ``-i`` instead of ``--test``.

.. code-block:: bash

	./intervene/intervene venn -i intervene/example_data/ENCODE_hESC/*.bed
  	./intervene/intervene upset -i intervene/example_data/ENCODE_hESC/*.bed
  	./intervene/intervene pairwise -i intervene/example_data/dbSUPER_mm9/*.bed

This will save the results in the current working directory with a folder named ``Intervene_results``. If you wish to save the results in a specific folder, you can type::

	intervene upset --test --output ~/path/to/your/folder

Interactive Shiny App
=====================
Intervene Shiny App is freely available at https://asntech.shinyapps.io/intervene

Support
========
If you have questions, or found any bug in the program, please write to us at ``aziz.khan[at]ncmm.uio.no``

Cite Us
=========
If you use Intervene please cite us: ``Khan A, Mathelier A: Intervene: a tool for intersection and visualization of multiple gene or genomic region sets. bioRxiv 2017, doi: https://doi.org/10.1101/109728``
