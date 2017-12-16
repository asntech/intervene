=================
Intervene modules
=================
Intervene provides three types of plots to visualize intersections of genomic regions and list sets. These are pairwise heatmap of N genomic region sets, classic Venn diagrams of genomic regions and list sets of up to 6-way and UpSet plots.

.. note:: By default the intersection genomic regions is computed using default parameters of `BedTools`. Intervene version > v0.6.0 now allows users to provide all the arguments available in BedTools' commands  by using **--bedtools-options**.

Venn diagram module 
===================

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

    intervene venn -i path/to/BED/files/*.bed

This will save the results in the current working directory with a folder named ``Intervene_results``. If you wish to save the results in a specific folder, you can type:

.. code-block:: bash

    intervene venn -i path/to/BED/files/*.bed --output ~/results/path

**Summary of options**

.. csv-table::
   :header: "Option", "Description"
   :widths: 10, 80

     "-h, --help","To show the help message and exit"
	 "-i, --input","Input genomic regions in (BED/GTF/GFF) format or lists of genes/SNPs IDs. For files in a directory use *.<extension>. e.g. *.bed"
	 "--type","{genomic,list}. Type of input sets. Genomic regions or lists of genes/SNPs. Default is ``genomic``"
	 "--names","Comma-separated list of names as labels for input files. If it is not set file names will be used as labels. For example: --names=A,B,C,D,E,F"
	 "--filenames","Use file names as labels instead. Default is ``False``"
	 "--bedtools-options","List any of the arguments available for bedtool’s intersect command. Type bedtools intersect --help to view all the options. For example: --bedtools-options f=0.8,r,etc"
	 "--colors","Comma-separated list of matplotlib-valid colors for fill. E.g., --colors=r,b,k"
	 "--bordercolors","Comma-separated list of matplotlib-valid colors for borders. E.g., --bordercolors=r,b,k"
	 "-o, --output","Output folder path where results will be stored. Default is current working directory."
	 "--save-overlaps","Save overlapping regions/names for all the combinations as bed/txt files. Default is ``False``"
	 "--figtype","{pdf,svg,ps,tiff,png} Figure type for the plot. e.g. --figtype svg. Default is ``pdf``"
	 "--figsize","Figure size as width and height.e.g. --figsize 12 12."
	 "--fontsize","Font size for the plot labels. Default is ``14``"
	 "--dpi","Dots-per-inch (DPI) for the output. Default is: ``300``"
	 "--fill","{number,percentage} Report number or  percentage of overlaps (Only if --type=list). Default is ``number``"
	 "--test","This will run the program on test data."


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

    intervene upset -i path/to/BED/files/*.bed

This will save the results in the current working directory with a folder named ``Intervene_results``. If you wish to save the results in a specific folder, you can type:

.. code-block:: bash

    intervene upset -i path/to/BED/files/*.bed --output ~/results/path


**Summary of options**

.. csv-table::
   :header: "Option", "Description"
   :widths: 10,80
   
	 "-h, --help", "show this help message and exit"
	 "-i, --input", "Input genomic regions in <BED/GTF/GFF/VCF> format or list files. For files in a directory use *.<ext>. e.g. *.bed"
	 "--type","Type of input sets. Genomic regions or lists of genes sets {genomic,list}. Default is ``genomic``"  
 	 "--names","Comma-separated list of names as labels for input files. If it is not set file names will be used as labels. For example: --names=A,B,C,D,E,F"
 	 "--filenames","Use file names as labels instead. Default is ``True``"
 	 "--bedtools-options","List any of the arguments available for bedtool’s intersect command. Type bedtools intersect --help to view all the options. For example: --bedtools-options f=0.8,r,etc"
	 "-o, --output","Output folder path where plots will store. Default is current working directory."
	 "--save-overlaps","Save overlapping regions/names for all the combinations as bed/txt files. Default is ``False``"
	 "--order", "The order of intersections of sets {freq,degree}. e.g. --order degree. Default is ``freq`` "
	 "--ninter", "Number of top intersections to plot. Default is ``30``"
	 "--showzero", "Show empty overlap combinations. Default is ``False``"
	 "--showsize", "Show intersection sizes above bars. Default is ``True``"
	 "--mbcolor", "Color of the main bar plot. Default is ``gray23``"
	 "--sbcolor", "Color of set size bar plot. Default is ``#56B4E9``"
	 "--mblabel", "The y-axis label of the intersection size bars. Default is ``No of Intersections``"
	 "--sxlabel", "The x-axis label of the set size bars. Default is ``Set size``"
	 "--figtype", "Figure type for the plot. e.g. --figtype svg {pdf,svg,ps,tiff,png} Default is ``pdf``"
	 "--figsize", "Figure size for the output plot (width,height)."
	 "--dpi", "Dots-per-inch (DPI) for the output. Default is ``300``"
	 "--scriptonly", "Set to generate Rscript only, if R/UpSetR package is not installed. Default is ``False``"
	 "--showshiny", "Print the combinations of intersections to input to Shiny App. Default is ``False``"


Pairwise intersection module
============================
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
	
	intervene pairwise -i path/to/BED/files/*.bed --type genomic --compute jaccard --htype tribar

This will save the results in the current working directory with a folder named ``Intervene_results``. If you wish to save the results in a specific folder, you can type:

.. code-block:: bash

    intervene pairwise -i path/to/BED/files/*.bed --type genomic --compute jaccard --htype tribar --output ~/results/path

**Summary of options**

.. csv-table::
   :header: "Option", "Description"
   :widths: 10, 80

	  "-h, --help","show this help message and exit"
	  "-i, --input","Input genomic regions in (BED/GTF/GFF) format. For files in a directory use *.<extension>. e.g. *.bed"
	  "--type","{genomic,list}. Type of input sets. Genomic regions or lists of genes/SNPs. Default is ``genomic``"
	  "--compute","Compute count/fraction of overlaps or statistical relationships. {``count``, ``frac``, ``jaccard``, ``fisher``, ``reldist``}"
	  " ","--compute=count - calculates the number of overlaps."
	  " ","--compute=frac - calculates the fraction of overlap."
	  " ","--compute=jaccard - calculate the Jaccard statistic. `Read more details here <http://bedtools.readthedocs.io/en/latest/content/tools/jaccard.html>`_"
	  " ","--compute=reldist - calculate the distribution of relative distances. `Read more details here <http://bedtools.readthedocs.io/en/latest/content/tools/reldist.html>`_"
	  " ","--compute=fisher - calculate Fisher`s statistic. `Read more details here <http://bedtools.readthedocs.io/en/latest/content/tools/fisher.html>`_"
	  " ","Note: For jaccard and reldist regions should be pre-shorted or set --sort``"
	  "--bedtools-options","List any of the arguments available for bedtool’s subcommands: interset, jaccard, fisher. Type `bedtools <subcommand> --help` to view all the options. For example: --bedtools-options f=0.8,r,etc."
	  " ","Note: --compute options count and frac uses BedTools' intersect command."
	  "--corr","Compute the correlation. By default set to False"
	  "--corrtype","Select the type of correlation from ``pearson``, ``kendall`` or ``spearman``."
	  " ","--corrtype=pearson: computes the Pearson correlation. (Default)"
	  " ","--corrtype=kendall: computes the Kendall correlation."
	  " ","--corrtype=spearman: computes the Spearman correlation."
	  " ", "Note: This only works if --corr is set."
	  "--htype","{tribar,color,pie,circle,square,ellipse,number,shade}. Heatmap plot type. Default is ``tribar``."
	  " ", "Read the below note for ``tribar`` option."
	  "--triangle","Show lower/upper triangle of the matrix as heatmap. Default is ``lower``"
	  "--diagonal", "Show the diagonal values in the heatmap. Default is ``False``."
 	  "--names","Comma-separated list of names as labels for input files. If it is not set file names will be used as labels. For example: --names=A,B,C,D,E,F"
 	  "--filenames","Use file names as labels instead. Default is ``False``."
	  "--sort","Set this only if your files are not sorted. Default is ``False``."
	  "--genome","Required argument if --compute=fisher. Needs to be a string assembly name such as ``mm10`` or ``hg38``"
	  "-o, --output","Output folder path where results will be stored. Default is current working directory."
	  "--barlabel","x-axis label of boxplot if --htype=tribar. Default is ``Set size``"
	  "--barcolor","Boxplot color (hex vlaue or name, e.g. blue). Default is ``#53cfff``."
	  "--fontsize","Label font size. Default is ``8``."
	  "--title","Heatmap main title. Default is ``Pairwise intersection``"
	  "--space","White space between barplt and heatmap, if --htype=tribar. Default is ``1.3``."
	  "--figtype","{pdf,svg,ps,tiff,png} Figure type for the plot. e.g. --figtype svg. Default is ``pdf``"
	  "--figsize","Figure size for the output plot (width,height). e.g.  --figsize 8 8"
	  "--dpi","Dots-per-inch (DPI) for the output. Default is: ``300``."
	  "--scriptonly", "Set to generate Rscript only, if R/Corrplot package is not installed. Default is ``False``"
	  "--test","This will run the program on test data."


.. note::  The option ``--htype=tribar`` will generate a horizontal bar plot with an adjacent heatmap rotated 45 degrees to show the lower triangle of the matrix comparing all sets of bars. If you want to view upper triangle, please ``--triangle upper``. It's only recomended to use ``tribar`` if ``compute`` is set to ``jaccard`` or ``fisher``.
