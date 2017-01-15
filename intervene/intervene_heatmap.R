#!/usr/bin/env Rscript
#Plot intersection diagrams using UpSetR package
#Author: Aziz Khan
#Email: aziz.khan@ncmm.uio.no

#================================================================#
args = commandArgs(trailingOnly=TRUE)
# test if there is at least one argument: if not, return an error
if (length(args) < 4) {
  stop("At least 4 arguments must be supplied", call.=FALSE)
}

intersection_matrix <- as.matrix(read.table(args[1]))

output_name <- args[3]

if(args[4] =='pdf') pdf(file=output_name, dpi=300)

if(args[4] =='svg') svg(file=output_name, dpi=300)

if(args[4] =='png') png(file=output_name,dpi=300)

x_label = 'Value'
test_type <- args[3]
if(test_type == 'frac') x_label <- 'Overlap fraction'
if(test_type == 'jaccard') x_label <- 'Jaccard index'
if(test_type == 'fisher') x_label <- 'Fisher two tailed'
if(test_type == 'count') x_label <- 'No. of overlap'

if(args[2] == 'heatmap2' || args[2] ==''){

	# install.packages("gplots")
	if (suppressMessages(!require("gplots"))) suppressMessages(install.packages("gplots"))
	suppressPackageStartupMessages(library("gplots"))
	if (suppressMessages(!require("RColorBrewer"))) suppressMessages(install.packages("RColorBrewer"))
	suppressPackageStartupMessages(library("RColorBrewer"))

	col <- colorRampPalette(brewer.pal(10, "RdYlBu"))(256)

	heatmap.2(intersection_matrix, scale = "none", col = col, key.title = NULL, main = "Pairewise Intersection",
		dendrogram = c('row'),
		Colv="Rowv",
        key.xlab = x_label,
        key.ylab = NULL,
        keysize = 1.5,
        margins = c(8, 8),
        trace = "none", density.info = "none")

	#Create D3 Heatmap
	if (suppressMessages(!require("devtools"))) suppressMessages(install.packages("devtools"))
	if (suppressMessages(!require("d3heatmap"))) suppressMessages(devtools::install_github("rstudio/d3heatmap"))
	if (suppressMessages(!require("htmlwidgets"))) suppressMessages(install.packages("htmlwidgets"))

	suppressPackageStartupMessages(library("d3heatmap"))
	suppressPackageStartupMessages(library("htmlwidgets"))
	
	map <- d3heatmap(scale(intersection_matrix), k_row = 4, k_col = 4)
	saveWidget(map, "intervene_d3heatmap.html")

	#print(paste0('You are done! Please check the plot @ ', output_name))


}else if(args[2] == 'corrplot'){
	
	if (suppressMessages(!require("corrplot"))) suppressMessages(install.packages("corrplot"))
	suppressPackageStartupMessages(library('corrplot'))

	#diag(intersection_matrix) = 0

	corrplot(intersection_matrix, method = 'color', order = 'hclust', cl.lim=c(0, 1))
	
	#print(paste0('You are done! Please check your plot', output_name))

} else if(args[2] == 'heatmap'){

	library("RColorBrewer")
	col <- colorRampPalette(brewer.pal(10, "RdYlBu"))(256)
	heatmap(intersection_matrix, scale = "none", col =  col)

	#heatmap(intersection_matrix, scale = "none", col = bluered(100), 
     #     trace = "none", density.info = "none")
}else{

		print('Something went wrong!')
}

invisible(dev.off())



