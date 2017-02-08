Up-to 6-way Venn module 
=======================

Once you have installed Intervene, you can type:

**Usage:**

.. code-block:: bash

    intervene venn [options]

**Help:**

.. code-block:: bash

    intervene venn --help

**Example:**

.. code-block:: bash

    intervene venn -i path/to/BED/files/*.bed --type jaccard --htype tribar

This will save the results in the current working directory with a folder named ``Intervene_test``. If you wish to save the results in a specific folder, you can type:

.. code-block:: bash

    intervene venn -i path/to/BED/files/*.bed --type jaccard --htype tribar --output ~/results/path


.. note::  This is a **note** box.


.. csv-table::
   :header: "Option", "Description", "Default"
   :widths: 10, 80, 10

   "**-i**", "Input file", 
   "Smith", "John, Junior", 20
