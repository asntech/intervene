__version__ = '0.7.7'

import sys
import os
from pybedtools import BedTool, helpers
from intervene import utils
import itertools
from intervene.modules.venn import list_venn

from rpy2.robjects.packages import importr
import rpy2.robjects as robjects

# class Intervene:
# 	def __init__(self, module, input):
# 		self.module = module
# 		self.input = input

# 	def upset(self):
# 		print("This is " + self.module)

# 	def venn(self):
# 		print("This is " + self.module)

#calss Venn(Intervene):

#------------------------------------------#
# 		   		  venn module 			   #
#------------------------------------------#
def venn(
	input=None, 
	type='genomic', 
	labels=None, 
	filenames=True, 
	style='Classical', 
	weighted=True, 
	bedtools_options=None, 
	output='./Intervene_results', 
	saveoverlaps=False, 
	overlapthresh=1, 
	title=None, 
	project='Intervene', 
	colors=None, 
	bordercolors=None,
	faces=False,
	figtype='pdf', 
	figsize=(7, 7), 
	fontsize=14, 
	dpi=300, 
	scriptonly=False, 
	test=False,
	):

	"""Venn diagram of intersection of genomic regions or list sets (upto 6-way)

    Create Venn diagram upto 6-way after intersection of genomic regions in (BED/GTF/GFF) format or list sets.

    Args:
        input (list): Input genomic regions in (BED/GTF/GFF) format or lists of genes/SNPs IDs.
        type (str): Type of input sets. Genomic regions or lists of genes/SNPs. Options are: genomic or list.
        labels (list): List of names as labels for input files. If it is not set file names will be used as labels.
        filenames (bool): Use file names as labels instead.
        style (str): Venn plot style. Classical, ChowRuskey etc. Default is Classical. Options are: 'Classical','ChowRuskey','Edwards','Squares','Battle'),
		weighted (bool): Generate weighted venn plots
    	bedtools_options (str): List any of the arguments available for bedtools intersect command. Type bedtools intersect --help to view all the options. For example: --bedtools-options f=0.8,r,etc.
    	output (str): Output folder path where results will be stored. Default is current working directory.
    	saveoverlaps (bool): Save overlapping regions/names for all the combinations as bed/txt.
    	overlap_thresh (int): Minimum threshold to save the overlapping regions/names as bed/txt.
    	title (str): Title of the plot.
    	project (str): Project name for the output.
    	colors (list): A list of colors for fill. E.g., --colors=blue,green,orange
    	bordercolors (list): A matplotlib-valid color for venn borders. E.g., --bordercolor=red.
    	figtype (str): Figure type for the plot. choices=('pdf','svg','ps','tiff','png')
    	figsize (tuple): Figure size as width and height.
    	fontsize (int): Font size for the plot labels.
    	dpi (int): Dots-per-inch (DPI) for the output.
    	scriptonly (bool): Set to generate Rscript only, if R/Vennerable package is not installed.
    	test (bool): This will run the program on test data.

    Returns:
        weights (dict): Overlap weights of sets as a dictionary
        labels (list): Set names
        file_path (str): Path for the output venn figure
    """
	
	try:
		Vennerable = importr('Vennerable')
		grdevices = importr('grDevices')
	except RRuntimeError:
		print("Unable to load Vennerable in R, make sure it's properly installed or set scriptonly")
		sys.exit(1)

	#get the label names
	if not labels:
		labels = utils.get_filenames(input)

	if type == 'genomic':
		weights = get_weights_genomic(input, labels)
	elif type == 'list':
		weights = get_weights_list(input, labels)
	else:
		print("Please use input data-type as genomic or list")
		sys.exit(1)

	venn_type = utils.get_venn_plot_type(style, len(labels))
	weighted = str(weighted).upper()
	plot_kwargs = {
    "type": venn_type,
    "doWeights": str(weighted).upper(), 
    "show": "list(Universe=FALSE, Faces="+str(faces).upper()+")"
    }

	venn_kwargs= {}

	weight_string = "c(" + ", ".join(["\'" + k + "\'=" + str(v) for k,v in weights.items() ]) + ")"
	ven_kw = ", ".join([k + " = " + v for k,v in venn_kwargs.items()])
	plot_kw = ", ".join([k + " = " + v for k,v in plot_kwargs.items()])
	labels  = "c(\'" + "\', \'".join(labels) + "\')"
	
	utils.create_dir(output)
	file_path =  output + "/venn.png"
	grdevices.png(file=file_path, width=512, height=512)
	robjects.r("plot(Venn(" + "Weight = " + weight_string + ", SetNames = " + labels + ", " + ven_kw + ")," + plot_kw +  ")")
	#robjects.r.plot(Vennerable.Venn(Weight=weight_string, SetNames=labels))
	grdevices.dev_off()

	return (weights, labels, file_path)

#------------------------------------------#
# 		   		  upset module 			   #
#------------------------------------------#
def upset(
		input=None, 
		type='genomic', 
		labels=None, 
		filenames=True, 
		bedtools_options=None, 
		output='./Intervene_results', 
		saveoverlaps=False, 
		overlapthresh=1, 
		project='Intervene', 
		order='freq', 
		ninter=30, 
		showzero=False,
		keep_order=False,
		showsize=True, 
		mbcolor='#ea5d4e', 
		sbcolor='#317eab', 
		mblabel='No. of Intersections', 
		sxlabel='Set size', 
		figtype='pdf', 
		figsize=(14, 8), 
		dpi=300, 
		scriptonly=False, 
		showshiny=False, 
		test=False,
	):
	"""Upset diagram of intersection of genomic regions or list sets (upto 6-way)

    Create Venn diagram upto 6-way after intersection of genomic regions in (BED/GTF/GFF) format or list sets.

    Args:
        input (list): Input genomic regions in (BED/GTF/GFF) format or lists of genes/SNPs IDs.
        type (str): Type of input sets. Genomic regions or lists of genes/SNPs. Options are: genomic or list.
        labels (list): List of names as labels for input files. If it is not set file names will be used as labels.
        filenames (bool): Use file names as labels instead.
        style (str): Venn plot style. Classical, ChowRuskey etc. Default is Classical. Options are: 'Classical','ChowRuskey','Edwards','Squares','Battle'),
		weighted (bool): Generate weighted venn plots
    	bedtools_options (str): List any of the arguments available for bedtools intersect command. Type bedtools intersect --help to view all the options. For example: --bedtools-options f=0.8,r,etc.
    	output (str): Output folder path where results will be stored. Default is current working directory.
    	saveoverlaps (bool): Save overlapping regions/names for all the combinations as bed/txt.
    	overlap_thresh (int): Minimum threshold to save the overlapping regions/names as bed/txt.
    	title (str): Title of the plot.
    	project (str): Project name for the output.
    	colors (list): A list of colors for fill. E.g., --colors=blue,green,orange
    	bordercolors (list): A matplotlib-valid color for venn borders. E.g., --bordercolor=red.
    	figtype (str): Figure type for the plot. choices=('pdf','svg','ps','tiff','png')
    	figsize (tuple): Figure size as width and height.
    	fontsize (int): Font size for the plot labels.
    	dpi (int): Dots-per-inch (DPI) for the output.
    	scriptonly (bool): Set to generate Rscript only, if R/Vennerable package is not installed.
    	test (bool): This will run the program on test data.

    Returns:
        weights (dict): Overlap weights of sets as a dictionary
        labels (list): Set names
        file_path (str): Path for the output venn figure
    """

	try:
		UpSetR = importr('UpSetR')
		grdevices = importr('grDevices')
	except RRuntimeError:
		print("Unable to load UpSetR in R, make sure it's properly installed or set scriptonly.")
		sys.exit(1)

	#get the label names
	if not labels:
		labels = utils.get_filenames(input)

	if type == 'genomic':
		weights = get_weights_genomic(input, labels)
	elif type == 'list':
		weights = get_weights_list(input, labels)
	else:
		print("Please use input data-type as genomic or list")
		sys.exit(1)

	utils.create_dir(output)

	expression_input = utils.get_upset_expression_input(weights, labels)
	print(expression_input)
	output_png =  output + "/upset.png"
	print("upset(fromExpression(" + expression_input + "))")
	#        temp_f.write(options.figtype+'("'+output_name+'", width='+str(options.dpi*options.figsize[0])+', height='+str(options.dpi*options.figsize[1])+', res='+str(options.dpi)+')\n')
	grdevices.png(file=output_png, width=900, height=512)
	robjects.r("upset(fromExpression(" + expression_input + "))")
	#UpSetR.upset(UpSetR.fromExpression(expression_input))
	grdevices.dev_off()

	return (weights,labels, output_png)


#------------------------------------------#
# 		   	    pairwise module 		   #
#------------------------------------------#
def pairwise():
	"""Venn diagram of intersection of genomic regions or list sets (upto 6-way)

    Create Venn diagram upto 6-way after intersection of genomic regions in (BED/GTF/GFF) format or list sets.

    Args:
        input (list): Input genomic regions in (BED/GTF/GFF) format or lists of genes/SNPs IDs.
        type (str): Type of input sets. Genomic regions or lists of genes/SNPs. Options are: genomic or list.
        labels (list): List of names as labels for input files. If it is not set file names will be used as labels.
        filenames (bool): Use file names as labels instead.
        style (str): Venn plot style. Classical, ChowRuskey etc. Default is Classical. Options are: 'Classical','ChowRuskey','Edwards','Squares','Battle'),
		weighted (bool): Generate weighted venn plots
    	bedtools_options (str): List any of the arguments available for bedtools intersect command. Type bedtools intersect --help to view all the options. For example: --bedtools-options f=0.8,r,etc.
    	output (str): Output folder path where results will be stored. Default is current working directory.
    	saveoverlaps (bool): Save overlapping regions/names for all the combinations as bed/txt.
    	overlap_thresh (int): Minimum threshold to save the overlapping regions/names as bed/txt.
    	title (str): Title of the plot.
    	project (str): Project name for the output.
    	colors (list): A list of colors for fill. E.g., --colors=blue,green,orange
    	bordercolors (list): A matplotlib-valid color for venn borders. E.g., --bordercolor=red.
    	figtype (str): Figure type for the plot. choices=('pdf','svg','ps','tiff','png')
    	figsize (tuple): Figure size as width and height.
    	fontsize (int): Font size for the plot labels.
    	dpi (int): Dots-per-inch (DPI) for the output.
    	scriptonly (bool): Set to generate Rscript only, if R/Vennerable package is not installed.
    	test (bool): This will run the program on test data.

    Returns:
        weights (dict): Overlap weights of sets as a dictionary
        labels (list): Set names
        file_path (str): Path for the output venn figure
    """

	return ("pairwise")



def get_weights_genomic(file_list, label_names, bedtools_options=None, overlap_thresh=1, save_overlaps=False, output="./Intervene_results"):
    '''
    Takes a list of sets a list of the sizes of non-overlapping intersections between them.
    
    Arguments:
        file_list -  List of list files to calculate weights
        label_names - Names of input files/sets
        bedtools_options - BEDTools additional options for intersect command
        overlap_thresh - Minimum threshold to save the overlapping regions/names as bed/txt.
        save_overlaps - Store combination of overlaps as individual text files.
        output - Output path to store combination of overlaps if save_overlaps is set to True
    '''

    assert len(file_list) == len(label_names), "Number of files must match the number of labels."

    #file_list = options.input
    #output = options.output

    kwargs = utils.map_bedtools_options(bedtools_options)

    N = len(file_list)
    
    # Generate a truth table of intersections to calculate 
    truth_table = [x for x in itertools.product("01", repeat=N)][1:]

    weights = {}

    for t in truth_table:
        ones = [BedTool(file_list[i]) for i in range(N) if t[i] =='1']
        zeros = [BedTool(file_list[i]) for i in range(N) if t[i] =='0']
        #report those entries in set A which do ovelap with other sets
        x = ones[0]
        if len(ones) > 1:
            for bed in ones[1:]:
                x = x.intersect(bed, u=True, **kwargs)
        #report those entries in set A which doesn't ovelap with other sets
        if len(zeros) > 0:
            #y = zeros[0]
            for bed in zeros[0:]:
                x = x.intersect(bed, v=True, **kwargs)
        X = (x).count()
        weights[''.join(t)] = X
        
        #save the intersected results
        if save_overlaps:
            if X >= overlap_thresh:
                file_name = ''
                name_itr = 0
                for name in t:
                    if name == '1':
                        file_name += '_'+label_names[name_itr]
                    name_itr +=1
                file_name = ''.join(t)+file_name
                utils.create_dir(output+'/sets')
                x.moveto(output+'/sets/'+file_name+'.bed')
        
        #delete all temp files
        helpers.cleanup()

    return (weights)

def get_weights_list(file_list, label_names, overlap_thresh=1, save_overlaps=False, output="./"):
    '''
    Takes a list of sets a list of the sizes of non-overlapping intersections between them 
    Arguments:
        file_list -  List of list files to calculate weights
        label_names - Names of input files/sets
        overlap_thresh - Minimum threshold to save the overlapping regions/names as bed/txt.
        save_overlaps - Store combination of overlaps as individual text files.
        output - Output path to store combination of overlaps if save_overlaps is set to True
    '''
    #files_list = options.input
    #output = options.output
    assert len(file_list) == len(label_names), "Number of files must match the number of labels."
    
    S =[]
    for f in file_list:
        with open(f) as f_open:
            S.append(set(f_open.read().splitlines()))
    N = len(S)
    # Generate a truth table of intersections to calculate 
    truth_table = [x for x in itertools.product("01", repeat=N)][1:]
    weights = {}
    for t in truth_table:
        ones = [S[i] for i in range(N) if t[i] =='1']
        zeros = [S[i] for i in range(N) if t[i] =='0']
        X = set.intersection(*ones)
        X.difference_update(*zeros)
        weights[''.join(t)] = len(X)

        #save the intersected results
        if save_overlaps:
            if len(X) >= overlap_thresh:
                file_name = ''
                name_itr = 0
                for name in t:
                    if name == '1':
                        file_name += '_'+label_names[name_itr]
                    name_itr +=1
                file_name = ''.join(t)+file_name
                utils.create_dir(output+'/sets')
                inter_file = open(output+'/sets/'+file_name+'.txt', 'w')
                inter_file.writelines('\n'.join(list(X)))
                inter_file.close()

    return(weights)


