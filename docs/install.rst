Installation
============

Prerequisites
-------------
InterVene requires:

	* Python (>= 2.7 or >= 3.3)
	* pybedtools (>= 1.6.1): https://daler.github.io/pybedtools/
	* R (>= )

If you already have a working installation of Python, the easiest way to install pybedtools and argparser is using pip::

	pip install pybedtools

	pip install argparser

or using conda::

	conda install -c bioconda pybedtools

Read more details about ''pybedtools'' installation: https://daler.github.io/pybedtools/main.html#

If you're setting up Python for the first time, we recommend to install it using Anaconda Python distribution http://continuum.io/downloads. These come with several helpful scientific and data processing libraries. These are available for platforms including Windows, Mac OSX and Linux. 


Install using `pip`
-------------------
You can install InterVene either from PyPi using pip or install it from the source. Please make sure you have already installed the above mentioned python libraries required to run InterVene.

Install from PyPi::

	pip install intervene

Install Intervene from `GitHub`
------------------------------

If you have `git` is installed, use this:

.. code-block:: bash

    git clone https://github.com/asntech/intervene.git
    cd intervene
    python setup.py install

Install from Intervene source
-----------------------------

.. code-block:: bash
	
	wget https://github.com/asntech/intervene/intervene-1.0.tar.gz
	tar -zxvf intervene-1.0.tar.gz
	cd intervene-1.0
	python setup.py install


