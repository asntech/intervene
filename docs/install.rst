============
Installation
============

Quick installation
==================

Install uisng bioconda
----------------------
.. code-block:: bash

	conda install -c bioconda intervene

This will install all the dependencies and you are ready to use Intervene. Make sure you have R installed.

Install using `pip`
-------------------
You can install Intervene from PyPi using pip.

Install from PyPi::

	pip install intervene

Prerequisites
=============
Intervene requires the following Python modules and R packages:

	* Python (=> 2.7 ): https://www.python.org/
	* BEDTools (Latest version): https://github.com/arq5x/bedtools2
	* pybedtools (>= 0.7.9): https://daler.github.io/pybedtools/
	* Pandas (>= 0.16.0): http://pandas.pydata.org/
	* Seaborn (>= 0.7.1): http://seaborn.pydata.org/
	* R (>= 3.0): https://www.r-project.org/
	* R packages including UpSetR, corrplot

Install BEDTools
-----------------
Intervene is using pybedtools, which is a Python wrapper for the BEDTools. BEDTools should be installed before using Intervene. It is recomended to have the latest version of the tool. Please read the installation instructions at https://github.com/arq5x/bedtools2 to install BEDTools, and make sure it is accessible through your PATH variable.

Install required Python modules
-------------------------------
Intervene takes care of the installation of all the required Python modules. If you already have a working installation of Python, the easiest way to install the required Python modules is by installing Intervene using ``pip``. If you're setting up Python for the first time, we recommend to install it using the Anaconda Python distribution http://continuum.io/downloads. These come with several helpful scientific and data processing libraries. These are available for platforms including Windows, Mac OSX and Linux.

If you want to install the required Python modules manually, you can use the following commands.

**Install pybedtools**

Install it from PyPi

.. code-block:: bash

	pip install pybedtools

or using conda

.. code-block:: bash

	conda install -c bioconda pybedtools

Read more details about ''pybedtools'' installation: https://daler.github.io/pybedtools/main.html

**Install Pandas**

Install it from PyPi

.. code-block:: bash

	pip install pandas

Or install with conda

.. code-block:: bash

	conda install pandas

Install required R packages
---------------------------
Intervene rquires three R packages, `UpSetR <https://cran.r-project.org/package=UpSetR>`_ , `corrplot <https://cran.r-project.org/package=corrplot>`_ for visualization and `Cairo <https://cran.r-project.org/package=Cairo>`_ to generate high-quality vector and bitmap figures. To install these, open R/RStudio and use the following command.

.. code-block:: R

    install.packages(c("UpSetR", "corrplot","Cairo"))

Install Intervene from source
=============================
You can install a development version by using ``git`` from our bitbucket repository at https://bitbucket.org/CBGR/intervene or Github. 


Install development version from `Bitbucket`
--------------------------------------------

If you have `git` installed, use this:

.. code-block:: bash

    git clone https://bitbucket.org/CBGR/intervene.git
    cd intervene
    python setup.py sdist install

Install development version from `GitHub`
-----------------------------------------
If you have `git` installed, use this:

.. code-block:: bash

    git clone https://github.com/asntech/intervene.git
    cd intervene
    python setup.py sdist install