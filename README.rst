.. image:: https://badge.fury.io/py/intervene.svg
    :target: https://badge.fury.io/py/intervene

.. image:: https://img.shields.io/github/issues/asntech/intervene.svg
	:target: https://github.com/asntech/intervene/issues

.. image:: https://img.shields.io/pypi/dm/intervene.svg
    :target:  https://pypi.python.org/pypi/intervene/

.. image:: https://img.shields.io/twitter/url/https/github.com/asntech/intervene.svg?style=social
	:target: https://twitter.com/intent/tweet?text=Intervene%20-%20a%20tool%20for%20intersection%20and%20visualization%20of%20multiple%20genomic%20region%20and%20gene%20sets%20https://github.com/asntech/intervene&url=%5Bobject%20Object%5D


Introduction
============
Intervene is a tool for intersection and visualization of multiple genomic region and gene sets.

**[Documentation](http://intervene.readthedocs.org)**

.. image:: http://intervene.readthedocs.io/en/latest/_images/Intervene_plots.png


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
-----------------
We are using pybedtools, which is Python wrapper for BEDTools. So, BEDTools should be installed before using Intervene. It's recomended to have a latest version, but if you have an older version already install, it should be fine. Please read the instructions at https://github.com/arq5x/bedtools2 to install BEDTools, and make sure it is on your path and you are able to call bedtools from any directory.


Install required Python modules
-------------------------------
Intervene takes care of the installation of all the required Python modules. If you already have a working installation of Python, the easiest way to install Intervene is by using ``pip``. If you're setting up Python for the first time, we recommend to install it using Anaconda Python distribution http://continuum.io/downloads. These come with several helpful scientific and data processing libraries. These are available for platforms including Windows, Mac OSX and Linux.


Install required R packages
---------------------------

Intervene rquires two R packages, ``UpSetR`` https://cran.r-project.org/package=UpSetR and ``corrplot`` https://cran.r-project.org/package=corrplot for visualization.

.. code-block:: R

    install.packages(c("UpSetR", "corrplot"))

Install Intervene
=================
You can install a stable version of Intervene by using ``pip`` from PyPi or a development version by using ``git`` from GitHub.

Install using `pip`
-------------------
You can install InterVene either from PyPi using pip or install it from the source. Please make sure you have already installed the above mentioned python libraries required to run InterVene.

Install from PyPi::

	pip install intervene

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
	
	intervene pairwise --help

	intervene venn --help

	intervene upset --help

Run Intervene on test data
--------------------------

To run Intervene using example data use the following command::

	intervene pairwise --test

	intervene venn --test

	intervene upset --test

This will save the results in the current working directory with a folder named ``Intervene_results``. If you wish to save the results in a specific folder, you can type::

	intervene upset --test --output ~/path/to/your/folder

Support
========
If you have questions, or found any bug in the program, please write to us at ``aziz.khan[at]ncmm.uio.no``

Cite Us
=========
If you use Intervene please cite us: ``Khan A. and Mathelier A., Intervene: a tool for intersection and visualization of multiple genomic region sets``
