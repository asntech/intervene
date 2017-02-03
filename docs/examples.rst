Example gallery
===============

Here we listed some examples to demonstrate how Intervene can be used to generated different types of set intersection plots.

Pairwise intersection heatmaps
------------------------------
In this example ... 

.. code-block:: bash

    intervene pairwise --help

Read more about the ``pairwise`` module here:

.. toctree::
   :maxdepth: 1
   
   pairwise


Venn diagrams
-------------
In this example ... 

.. code-block:: bash

    intervene pairwise --help

Read more about the ``venn`` diagrams module here:

.. toctree::
   :maxdepth: 1
   
   venn


UpSet plots
-----------
In this example ... 

.. code-block:: bash

    intervene pairwise --help

Read more about the ``upset`` module:

.. toctree::
   :maxdepth: 1
   
   upset


In this example ... 

.. code-block:: bash

    intervene pairwise --help
   

Usage:

.. code-block:: bash

    intervene pairwise -i path/to/BED/files/*.bed --type jaccard --htype tribar


This will save the results in the current working directory with a folder named ``Intervene_test``. If you wish to save the results in a specific folder, you can type:

.. code-block:: bash

    intervene pairwise -i path/to/BED/files/*.bed --type jaccard --htype tribar --output ~/results/path
	