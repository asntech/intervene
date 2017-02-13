====================
How to use Intervene
====================

Once you have installed Intervene, you can type:

.. code-block:: bash

    intervene --help

This will show the main help, which list three subcommands/modules, including ``venn``, ``upset``, ``pairwise``.

To view the help for the individual subcommands, please type:

You can view ``venn`` module help by typing this commman:

.. code-block:: bash

	intervene venn --help

You can view ``upset`` module help by typing this commman:

.. code-block:: bash

	intervene upset --help

You can view ``pairwise`` module help by typing this commman:

.. code-block:: bash

	intervene pairwise --help
	

Run Intervene on test data
==========================

To run Intervene's each module using example data use the following commands.

To run ``venn`` module with test data, type this;

.. code-block:: bash

	intervene venn --test

To run ``upset`` module with test data, type this;

.. code-block:: bash

	intervene upset --test

To run ``pairwise`` module with test data, type this;

.. code-block:: bash

	intervene pairwise --test

These commands will save the results in the current working directory with a folder named ``Intervene_results``. If you wish to save the results in a specific folder, you can type:

.. code-block:: bash

	intervene <module_name> --test --output ~/path/to/your/results/folder
