Intervene modules
=================

Intervene provides three types of plots to visualize intersections of genomic regions and list sets. These are pairwise heatmap of N genomic region sets, classic Venn diagrams of genomic regions and list sets of up to 6-way and UpSet plots.


Venn diagram module 
-------------------

Once you have installed Intervene, you can type:

**Usage:**

.. code-block:: bash

    intervene venn [options]

.. note:: Please scroll down to see a detailed summary of available **options**.

**Help:**

.. code-block:: bash

    intervene venn --help

**Example:**

.. code-block:: bash

    intervene venn -i path/to/BED/files/*.bed --type jaccard --htype tribar

This will save the results in the current working directory with a folder named ``Intervene_results``. If you wish to save the results in a specific folder, you can type:

.. code-block:: bash

    intervene venn -i path/to/BED/files/*.bed --type jaccard --htype tribar --output ~/results/path

**Summary of options**

.. csv-table::
   :header: "Option", "Description"
   :widths: 5, 30

     "-h, ---help","To show the help message and exit"
	 "-i","Input genomic regions in (BED/GTF/GFF) format or lists of genes/SNPs IDs. For files in a directory use *.<extension>. e.g. *.bed"
	 "--type","{genomic,list}. Type of input data sets. Genomic regions or lists of genes/SNPs. Default is ``genomic``"
	 "--names","Comma-separated list of names as labels for input files. Default is: --names=A,B,C,D,E,F"
	 "--filenames","Use file names as labels instead. Default is ``False``"             
	 "--colors","Comma-separated list of matplotlib-valid colors. E.g., --colors=r,b,k"
	 "-o, --output","Output folder path where results will be stored. Default is current working directory."
	 "--figtype","{pdf,svg,ps,tiff,png} Figure type for the plot. e.g. --figtype svg. Default is ``pdf``"
	 "--figsize","Figure size as width and height.e.g. --figsize 12 12."
	 "--dpi","Dots-per-inch (DPI) for the output. Default is: ``300``"
	 "--fill","{number,percentage} Report number or  percentage of overlaps (Only if --type=list). Default is ``number``"
	 "--test","This will run the program on test data."


UpSet plot module
-----------------

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

This will save the results in the current working directory with a folder named ``Intervene_results``. If you wish to save the results in a specific folder, you can type:

.. code-block:: bash

    intervene upset -i path/to/BED/files/*.bed --type jaccard --htype tribar --output ~/results/path


**Summary of options**

.. csv-table::
   :header: "Option", "Description"
   :widths: 5,30
   
	 "-h, --help", "show this help message and exit"
	 "-i, --input", "Input genomic regions in <BED/GTF/GFF/VCF> format or list files. For files in a directory use *.<ext>. e.g. *.bed"
	 "--type","Type of input sets. Genomic regions or lists of genes sets {genomic,list}. Default is ``genomic``"  
	 "--names","Comma-separated list of names for input files. Default is``--names=A,B,C,D,E,F``"
	 "--filenames","Use file names as labels instead. Default is ``False``"
	 "-o, --output","Output folder path where plots will store. Default is current working directory."
	 "--order", "The order of intersections of sets {freq,degree}. e.g. --order degree. Default is ``freq`` "
	 "--ninter", "Number of top intersections to plot. Default is ``40``"
	 "--showzero", "Show empty overlap combinations. Default is ``False``"
	 "--showsize", "Show intersection sizes above bars. Default is ``False``"
	 "--mbcolor", "Color of the main bar plot. Default is ``gray23``"
	 "--sbcolor", "Color of set size bar plot. Default is ``#56B4E9``"
	 "--mblabel", "The y-axis label of the intersection size bars. Default is ``No of Intersections``"
	 "--sxlabel", "The x-axis label of the set size bars. Default is ``Set size``"
	 "--figtype", "Figure type for the plot. e.g. --figtype svg {pdf,svg,ps,tiff,png} Default is ``pdf``"
	 "--figsize", "Figure size for the output plot (width,height)"
	 "--dpi", "Dots-per-inch (DPI) for the output. Default is ``300``"
	 "--run", "Run Rscript if R and UpSetR package is installed. Default is ``True``"
  
Pairwise intersection module
----------------------------

Once you have installed Intervene, you can type:

**Usage:**

.. code-block:: bash

    intervene pairwise [options]


.. note::  Please scroll down to see a detailed summary of available **options**.


**Help:**

.. code-block:: bash

    intervene pairwise --help

**Example:**

.. code-block:: bash
	
	intervene pairwise -i path/to/BED/files/*.bed --type jaccard --htype tribar

This will save the results in the current working directory with a folder named ``Intervene_results``. If you wish to save the results in a specific folder, you can type:

.. code-block:: bash

    intervene pairwise -i path/to/BED/files/*.bed --type jaccard --htype tribar --output ~/results/path


**Summary of options**

.. csv-table::
   :header: "Option", "Description"
   :widths: 10, 80

	  "-h, --help","show this help message and exit"
	  "-i","Input genomic regions in (BED/GTF/GFF) format. For files in a directory use *.<extension>. e.g. *.bed"
	  "--type","Report count/fraction of overlaps or statistical relationships. {``count`` ``frac`` ``jaccard`` ``fisher`` ``reldist``}"
	  " ","--type=count - calculates the number of overlaps."
	  " ","--type=frac - calculates the fraction of overlap."
	  " ","--type=jaccard - calculate the Jaccard statistic."
	  " ","--type=reldist - calculate the distribution of relative distances."
	  " ","--type=fisher - calculate Fisher`s statistic."
	  " ","Default is ``frac``"

	  "--htype*","{tribar,color,pie,circle,square,ellipse,number,shade}. Heatmap plot type. Default is ``pie``."
	  "--names*","Comma-separated list of names for input files. Default is base name of input files."
	  "--filenames*","Use file names as labels instead. Default is ``False``."
	  "--sort*","Set this only if your files are not sorted. Default is ``False``."
	  "--genome*","Required argument if --type=fisher. Needs to be a string assembly name such as ``mm10`` or ``hg38``"
	  "-o, --output*","Output folder path where results will be stored. Default is current working directory."
	  "--barlabel*","x-axis label of boxplot if --htype=tribar. Default is ``Set size``"
	  "--barcolor*","Boxplot color (hex vlaue or name, e.g. blue). Default is ``#53cfff``."
	  "--fontsize*","Label font size. Default is ``8``."
	  "--title*","Heatmap main title. Default is ``Pairwise intersection``"
	  "--space*","White space between barplt and heatmap, if --htype=tribar. Default is ``1.3``."
	  "--figtype*","{pdf,svg,ps,tiff,png} Figure type for the plot. e.g. --figtype svg. Default is ``pdf``"
	  "--figsize*","Figure size for the output plot (width,height). e.g.  --figsize 8 8"
	  "--dpi*","Dots-per-inch (DPI) for the output. Default is: ``300``."
	  "--test*","This will run the program on test data."

