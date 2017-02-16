====================
How to use Intervene
====================

Once you have installed Intervene, you can type:

.. code-block:: bash

    intervene --help

This will show the main help, which lists the three subcommands/modules: ``venn``, ``upset``, and ``pairwise``.

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

To run Intervene using example data, use the following commands.

To run ``venn`` module with test data, type

.. code-block:: bash

	intervene venn --test

To run ``upset`` module with test data, type

.. code-block:: bash

	intervene upset --test

To run ``pairwise`` module with test data, type

.. code-block:: bash

	intervene pairwise --test

These subcommands will save the results in the current working directory with a folder named ``Intervene_results``. If you wish to save the results in a specific folder, you can type:

.. code-block:: bash

	intervene <module_name> --test --output ~/path/to/your/results/folder
