'''
Created on 7 Jan 2015

@author: murrayking
'''
from __future__ import print_function
import glob
import os
import zipfile

rootDir = "/Users/murrayking/Downloads/terr50_cesh_gb/data/nt"
outPutDir = "/Users/murrayking/Documents/peeblescontours"
# os.chdir(rootDir)
# for file in glob.glob("*.zip"):
#     zf = os.path.join(rootDir, file)
#     with zipfile.ZipFile(zf, "r") as z:
#        z.extractall(outPutDir)
#         
#merge 

os.chdir(outPutDir)
files = glob.glob("*_line.shp")
print(len(files))
for i in range(0, len(files)):
    if i==0:
        os.system("pwd ")
        print(files[i])
        os.system("ogr2ogr file_merged.shp " + files[i])
    else:
        os.system("ogr2ogr -update -append file_merged.shp "+ files[i] +" -nln file_merged")
    