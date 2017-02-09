How to use Intervene
====================

Once you have installed Intervene, you can type:

.. code-block:: bash

    intervene --help

This will show the main help, which list three subcommands/modules, including ``venn``, ``upset``, ``pairwise``.

To view the help for the individual subcommands, ``venn``, ``upset`` and ``pairwise``type:


.. code-block:: bash

	intervene venn --help

.. code-block:: bash

	intervene upset --help

.. code-block:: bash

	intervene pairwise --help
	

Run Intervene on test data
--------------------------

To run Intervene's each module using example data use the following commands.

.. code-block:: bash

	intervene venn --test

.. code-block:: bash

	intervene upset --test

.. code-block:: bash

	intervene pairwise --test

This will save the results in the current working directory with a folder named ``Intervene_results``. If you wish to save the results in a specific folder, you can type::

	intervene upset --test --output ~/path/to/your/results/folder
