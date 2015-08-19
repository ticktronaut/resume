#! /usr/bin/python

import os

for files in os.listdir("."):
	if files.endswith(".svg"):
		svgFile = open(files, 'rb')
		os.system("inkscape --without-gui --file=" + files +  " --export-pdf=" + os.path.splitext(files)[0] + ".pdf")
