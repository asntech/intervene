Pairwise intersection module
=============================

Once you have installed Intervene, you can type:

**Usage:**

.. code-block:: bash

    intervene pairwise [options]

**Help:**

.. code-block:: bash

    intervene pairwise --help

**Example:**

.. code-block:: bash
	
	intervene pairwise -i path/to/BED/files/*.bed --type jaccard --htype tribar

This will save the results in the current working directory with a folder named ``Intervene_test``. If you wish to save the results in a specific folder, you can type:

.. code-block:: bash

    intervene pairwise -i path/to/BED/files/*.bed --type jaccard --htype tribar --output ~/results/path


.. note::  This is a **note** box.


.. csv-table::
   :header: "Option", "Description"
   :widths: 10, 80

	  "*-h, --help*","show this help message and exit"
	  "*-i*","Input genomic regions in (BED/GTF/GFF) format. For files in a directory use *.<extension>. e.g. *.bed"
	  "*--type*","Report count/fraction of overlaps or statistical relationships. {``count`` ``frac`` ``jaccard`` ``fisher`` ``reldist``} Default is ``frac``"
	  "*--type=count*","calculates the number of overlaps."
	  "*--type=frac*","calculates the fraction of overlap."
	  "*--type=jaccard*","calculate the Jaccard statistic."
	  "*--type=reldist*","calculate the distribution of relative distances."
	  "*--type=fisher*","calculate Fisher`s statistic."
	  "*--htype*","{tribar,color,pie,circle,square,ellipse,number,shade}. Heatmap plot type. Default is ``pie``."
	  "*--names*","Comma-separated list of names for input files. Default is base name of input files."
	  "*--filenames*","Use file names as labels instead. Default is ``False``."
	  "*--sort*","Set this only if your files are not sorted. Default is ``False``."
	  "*--genome*","Required argument if --type=fisher. Needs to be a string assembly name such as ``mm10`` or ``hg38``"
	  "*-o, --output*","Output folder path where results will be stored. Default is current working directory."
	  "*--barlabel*","x-axis label of boxplot if --htype=tribar. Default is ``Set size``"
	  "*--barcolor*","Boxplot color (hex vlaue or name, e.g. blue). Default is ``#53cfff``."
	  "*--fontsize*","Label font size. Default is ``8``."
	  "*--title*","Heatmap main title. Default is ``Pairwise intersection``"
	  "*--space*","White space between barplt and heatmap, if --htype=tribar. Default is ``1.3``."
	  "*--figtype*","{pdf,svg,ps,tiff,png} Figure type for the plot. e.g. --figtype svg. Default is ``pdf``"
	  "*--figsize*","Figure size for the output plot (width,height). e.g.  --figsize 8 8"
	  "*--dpi*","Dots-per-inch (DPI) for the output. Default is: ``300``."
	  "*--test*","This will run the program on test data."
