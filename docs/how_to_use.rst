====================
How to use Intervene
====================

Once you have installed Intervene, you can type:

.. code-block:: bash

    intervene --help

This will show the main help, which lists the three subcommands/modules: ``venn``, ``upset``, and ``pairwise``.

.. code-block:: bash

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

To view the help for the individual subcommands, please type:

To view ``venn`` module help, type

.. code-block:: bash

	intervene venn --help

To view ``upset`` module help, type

.. code-block:: bash

	intervene upset --help

To view ``pairwise`` module help, type

.. code-block:: bash

	intervene pairwise --help
	

Run Intervene on test data
==========================

To run Intervene using example data, use the following commands. To access the test data make sure you have ``sudo`` or ``root`` access.

To run ``venn`` module with test data, type

.. code-block:: bash

	intervene venn --test

To run ``upset`` module with test data, type

.. code-block:: bash

	intervene upset --test

To run ``pairwise`` module with test data, type

.. code-block:: bash

	intervene pairwise --test


If you have installed Intervene locally from the source code, you may have problem to find test data. You can download the test data here https://github.com/asntech/intervene/tree/master/intervene/example_data and point to it using ``-i`` instead of ``--test``.

.. code-block:: bash

	./intervene/intervene venn -i intervene/example_data/ENCODE_hESC/*.bed
  	./intervene/intervene upset -i intervene/example_data/ENCODE_hESC/*.bed
  	./intervene/intervene pairwise -i intervene/example_data/dbSUPER_mm9/*.bed
  

These subcommands will save the results in the current working directory with a folder named ``Intervene_results``. If you wish to save the results in a specific folder, you can type:

.. code-block:: bash

	intervene <module_name> --test --output ~/path/to/your/results/folder
