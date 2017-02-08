#!/usr/bin/env Rscript
#Pairwise intersection heatmap using corrplot package
#Author: Aziz Khan
#Email: aziz.khan@ncmm.uio.no

#================================================================#
args = commandArgs(trailingOnly=TRUE)
# test if there is at least one argument: if not, return an error
if (length(args) < 4) {
  stop("At least 4 arguments must be supplied", call.=FALSE)
}

intersection_matrix <- as.matrix(read.table(args[1]))

output_name <- paste0(args[4],'_',args[3])

#print(output_name)

res = args[7]

if(args[5] =='pdf') pdf(file=paste0(output_name,'.',args[5]))

if(args[5] =='svg') svg(file=paste0(output_name,'.',args[5]))

if(args[5] =='png') png(file=paste0(output_name,'.',args[5]))

if(args[5] =='tiff') tiff(file=paste0(output_name,'.',args[5]))

if(args[5] =='ps') postscript(file=paste0(output_name,'.',args[5]))


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
		dendrogram = c('none'),
		Colv="Rowv",
        key.xlab = x_label,
        key.ylab = NULL,
        keysize = 1.5,
        margins = c(8, 8),
        trace = "none", density.info = "none")
	invisible(dev.off())

	#Create D3 Heatmap
	if (suppressMessages(!require("d3heatmap"))){
			if (suppressMessages(!require("devtools"))) suppressMessages(install.packages("devtools"))

			suppressPackageStartupMessages(library("devtools"))

			suppressMessages(devtools::install_github("rstudio/d3heatmap"))

		}

	if (suppressMessages(!require("htmlwidgets"))) suppressMessages(install.packages("htmlwidgets"))

	suppressPackageStartupMessages(library("d3heatmap"))
	suppressPackageStartupMessages(library("htmlwidgets"))
	
	map <- d3heatmap(scale(intersection_matrix), k_row = 4, k_col = 4)
	saveWidget(map, paste0(output_name,"_D3Heatmap.html"))

	#print(paste0('You are done! Please check the plot @ ', output_name))

}else if(args[2] == 'corrplot'){
	
	if (suppressMessages(!require("corrplot"))) suppressMessages(install.packages("corrplot"))
	suppressPackageStartupMessages(library('corrplot'))

	#diag(intersection_matrix) = 0

	corrplot(intersection_matrix, method = 'color', title = "", is.corr = FALSE, cl.lim=c(min(intersection_matrix), max(intersection_matrix)))
	
	#print(paste0('You are done! Please check your plot', output_name))

} else if(args[2] == 'heatmap'){

	library("RColorBrewer")
	col <- colorRampPalette(brewer.pal(10, "RdYlBu"))(256)
	heatmap(intersection_matrix, scale = "none", col =  col)

	#heatmap(intersection_matrix, scale = "none", col = bluered(100), 
     #     trace = "none", density.info = "none")
}else{

	if (suppressMessages(!require("corrplot"))) suppressMessages(install.packages("corrplot"))
	suppressPackageStartupMessages(library('corrplot'))

	#diag(intersection_matrix) = 0

	#corrplot(intersection_matrix, method = args[2], title = "", is.corr = FALSE, cl.lim=c(min(intersection_matrix), max(intersection_matrix)))
	#print('Something went wrong!')
	corrplot(intersection_matrix, method = args[2], title=args[6], tl.col='black', tl.cex=0.8, is.corr = FALSE, diag=FALSE, addrect = 1, mar=c(0,0,2,1), rect.col = "black")

	invisible(dev.off())
}




