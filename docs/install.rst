Installation
############

Prerequisites
=============
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

If you already have a working installation of Python, the easiest way to install required Python modules is by using ``pip``. If you're setting up Python for the first time, we recommend to install it using Anaconda Python distribution http://continuum.io/downloads. These come with several helpful scientific and data processing libraries. These are available for platforms including Windows, Mac OSX and Linux.

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

**Install argparser**

.. code-block:: bash
	
	pip install argparser


Install required R packages
---------------------------
Intervene rquires two R packages, ``UpSetR`` https://cran.r-project.org/package=UpSetR
 and ``corrplot`` https://cran.r-project.org/package=corrplot
 for visualization.

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



