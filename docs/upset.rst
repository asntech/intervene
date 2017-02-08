UpSet plot module
=================

Once you have installed Intervene, you can type:

**Usage:**

.. code-block:: bash

    intervene upset [options]

.. note::  Please scroll down to see a detailed summary of available **options**.

**Help:** You can also see list of options by typing this on the terminal.

.. code-block:: bash

    intervene upset --help

**Example:**

.. code-block:: bash

    intervene upset -i path/to/BED/files/*.bed --type jaccard --htype tribar

This will save the results in the current working directory with a folder named ``Intervene_test``. If you wish to save the results in a specific folder, you can type:

.. code-block:: bash

    intervene upset -i path/to/BED/files/*.bed --type jaccard --htype tribar --output ~/results/path


.. note::  This is a **note** box.


**Summary of options**

.. csv-table::
   :header: "Option", "Description", "Default"
   :widths: auto
   
   "*-h, --help*", "show this help message and exit", " "
   "*-i, --input*", "Input genomic regions in <BED/GTF/GFF/VCF> format or list files. For files in a directory use *.<ext>. e.g. *.bed", " "
   "*--type*","Type of input sets. Genomic regions or lists of genes sets {genomic,list}.", "``genomic``"  
   "*--names*","Comma-separated list of names for input files. ", "``--names=A,B,C,D,E,F``"
   "*--filenames*", "Use file names as labels instead.", "``False``"
   "*-o, --output*", "Output folder path where plots will store. ", "current working directory."
   "*--order*", "The order of intersections of sets {freq,degree}. e.g. --order degree.", "``freq`` "
   "*--ninter*", "Number of top intersections to plot.", "``40``"
   "*--showzero*", "Show empty overlap combinations.", "``False``"
   "*--showsize*", "Show intersection sizes above bars.", "``False``"
   "*--mbcolor*", "Color of the main bar plot.", "``gray23``"
   "*--sbcolor*", "Color of set size bar plot.", "``#56B4E9``"
   "*--mblabel*", "The y-axis label of the intersection size bars. ", "``No of Intersections``"
   "*--sxlabel*", "The x-axis label of the set size bars. ", "``Set size``"
   "*--figtype*", "Figure type for the plot. e.g. --figtype svg {pdf,svg,ps,tiff,png}.","``pdf``"
   "*--figsize*", "Figure size for the output plot (width,height).","``(10, 6)``"
   "*--dpi*", "Dots-per-inch (DPI) for the output. ", "``300``"
   "*--run*", "Run Rscript if R and UpSetR package is installed. ", "``True``"
	
   
  

