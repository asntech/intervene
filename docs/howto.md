How to use Intervene
====================

Once you have installed Intervene, you can type:

	intervene --help

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

This will save the results in the current working directory with a folder named ``Intervene_test``. If you wish to save the results in a specific folder, you can type::

	intervene upset --test --output ~/path/to/your/folder/file_name.pdf
