#! /usr/bin/python

import os
import pyqrcode

print "Create qr-code."
# create qrcodes
url = pyqrcode.create("github.com/nerdOmat/resume")
url.svg('../images/qr.svg', scale=10)
