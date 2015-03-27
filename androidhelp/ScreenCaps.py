'''
Created on 23 Jan 2015

@author: murrayking
'''

import os


import PIL.Image
from PIL import Image


abdLoc = '/home/murray/Android/Sdk/platform-tools/adb'

os.system( abdLoc +" shell screencap -p /sdcard/screen.png")
os.system( abdLoc +" pull /sdcard/screen.png")
os.system( abdLoc +" shell rm /sdcard/screen.png")

os.system("pwd")



i = 1
while os.path.exists('/home/murray/workspace/pythonscripts/androidhelp/screenshot%s.png' % i):
    i += 1

outfile = '/home/murray/workspace/pythonscripts/androidhelp/screenshot%s.png' % i
infile = '/home/murray/workspace/pythonscripts/androidhelp/screen.png'
os.system("cp " + infile + " " + outfile);