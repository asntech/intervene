#!/usr/bin/env Rscript
#Plot intersection diagrams using UpSetR package
#Author: Aziz Khan
#Email: aziz.khan@ncmm.uio.no

#================================================================#
args = commandArgs(trailingOnly=TRUE)
# test if there is at least one argument: if not, return an error
if (length(args) < 3) {
  stop("At least 3 arguments must be supplied", call.=FALSE)
}

if (suppressMessages(!require("UpSetR"))) suppressMessages(install.packages("UpSetR"))

suppressMessages(library("UpSetR"))

output_name <- args[3]

print(args[4])

#listInput <- list(one = c(1, 2, 3, 5, 7, 8, 11, 12, 13), two = c(1, 2, 4, 5, 
 #   10), three = c(1, 5, 6, 7, 8, 9, 10, 12, 13))
if(args[1] == 'list'){

	if (args[2] == 3){
		input_data <- list('A' = c(scan(args[5], character(), quote = "\n")),B = c(scan(args[6], character(), quote = "\n")),
		C= c(scan(args[7], character(), quote = "\n")))

		pdf(output_name, width=8, height=5)
		upset(fromList(input_data), empty.intersections = "on", main.bar.color='brown',sets.bar.color='blue',
			order.by = "freq", mainbar.y.label = "No of Intersections", sets.x.label = "Set Size")
		dev.off()

	}else if (args[2] == 4){
		input_data <- list('A' = c(scan(args[5], character(), quote = "\n")),B = c(scan(args[6], character(), quote = "\n")),
		C= c(scan(args[7], character(), quote = "\n")), D = c(scan(args[8], character(), quote = "\n")) )

		pdf(output_name, width=8, height=5)
		upset(fromList(input_data), empty.intersections = "on", main.bar.color='brown',sets.bar.color='blue',
			order.by = "freq", mainbar.y.label = "No of Intersections", sets.x.label = "Set Size")
		dev.off()

	}else if (args[2] == 5){
		input_data <- list('A' = c(scan(args[5], character(), quote = "\n")),B = c(scan(args[6], character(), quote = "\n")),
		C= c(scan(args[7], character(), quote = "\n")), D = c(scan(args[8], character(), quote = "\n")),E = c(scan(args[9], character(), quote = "\n")) )

		pdf(output_name, width=8, height=5)
		upset(fromList(input_data), empty.intersections = "on", main.bar.color='brown',sets.bar.color='blue',
			order.by = "freq", mainbar.y.label = "No of Intersections", sets.x.label = "Set Size")
		dev.off()
		
	}else if (args[2] == 6){
		input_data <- list('A' = c(scan(args[5], character(), quote = "\n")),B = c(scan(args[6], character(), quote = "\n")),
		C = c(scan(args[7], character(), quote = "\n")), D = c(scan(args[8], character(), quote = "\n")), 
		E = c(scan(args[9], character(), quote = "\n")), F = c(scan(args[10], character(), quote = "\n")) )

		pdf(output_name, width=8, height=5)

		upset(fromList(input_data), nsets=args[2], main.bar.color='brown',sets.bar.color='blue',
			order.by = "freq", mainbar.y.label = "No of Intersections", sets.x.label = "Set Size")
		dev.off()

	}
	else{

		print('Something went wrong!')
	}
}

if(args[1] == 'genomic'){

if(args[5] =='pdf') pdf(file=paste0(output_name,'.',args[5]),width=8, height=5)

if(args[5] =='svg') svg(file=paste0(output_name,'.',args[5]),width=8, height=5)

if(args[5] =='png') png(file=paste0(output_name,'.',args[5]),width=8, height=5)


expressionInput <- source(args[3])

#pdf(output_name, width=8, height=5)
upset(fromExpression(expressionInput), nsets=args[2], main.bar.color='brown',sets.bar.color='blue',
			order.by = "freq", mainbar.y.label = "No of Intersections", sets.x.label = "Set Size")

invisible(dev.off())

}

