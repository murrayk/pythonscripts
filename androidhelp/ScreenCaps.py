'''
Created on 23 Jan 2015

@author: murrayking
'''

import os


import PIL.Image
from PIL import Image


abdLoc = '/Users/murrayking/Library/Android/sdk/platform-tools/adb'

os.system( abdLoc +" shell screencap -p /sdcard/screen.png")
os.system( abdLoc +" pull /sdcard/screen.png")
os.system( abdLoc +" shell rm /sdcard/screen.png")

os.system("pwd")


size = 600, 600
i = 1
while os.path.exists('/Users/murrayking/Documents/workspace2/TestPython/androidhelp/screensmaller%s.jpg' % i):
    i += 1

outfile = '/Users/murrayking/Documents/workspace2/TestPython/androidhelp/screensmaller%s.jpg' % i
infile = '/Users/murrayking/Documents/workspace2/TestPython/androidhelp/screen.png'
if infile != outfile:
    try:
        im = PIL.Image.open(infile)
        im.thumbnail(size, Image.ANTIALIAS)
        im.save(outfile, "JPEG")
    except IOError:
        print "cannot create thumbnail for '%s'" % infile