#! /usr/bin/python

import os
import pyqrcode

print "Create qr-code."
# create qrcodes
url = pyqrcode.create("github.com/nerdOmat/resume")
url.svg('../images/qr.svg', scale=2.25)

print "Convert qr-code from svg to png."
os.system("inkscape --without-gui --export-dpi=150 --file=../images/qr.svg --export-png=../images/qr.png")
#os.system("mogrify -resize 55% ../images/qr.png")
