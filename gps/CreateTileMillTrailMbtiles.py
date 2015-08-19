'''
Created on 1 Mar 2015

@author: murray
'''

import os
from os.path import expanduser
home = expanduser("~")

import subprocess
mbtilesDir = home + "/merge-mbtiles/"
os.system("rm -rf " + mbtilesDir)
os.system("mkdir " + mbtilesDir)

os.chdir('/Users/murray/Applications/TileMill.app/Contents/Resources')


def createInnersTileCreationCommands():
    createCentralTilesInners = './index.js export OSMBright ~/merge-mbtiles/central.mbtiles --minzoom=0 --maxzoom=18 --format=mbtiles --bbox="-3.061,55.5807,-3.0059,55.6202" --scale=2.5 --metatile=15'
    createSurroundingTilesInners = './index.js export OSMBright ~/merge-mbtiles/surrounding.mbtiles --minzoom=0 --maxzoom=14 --format=mbtiles --bbox="-3.2195,55.5069,-2.8144,55.6965" --scale=2.5 --metatile=15'
    return (createCentralTilesInners, createSurroundingTilesInners)

def createGlentressTileCreationCommands():
    createCentralTilesGlentress = './index.js export OSMBright ~/merge-mbtiles/central.mbtiles --minzoom=0 --maxzoom=18 --format=mbtiles --bbox="-3.1756,55.6437,-3.103,55.6908" --scale=2.5 --metatile=15'
    createSurroundingTilesGlentress = './index.js export OSMBright ~/merge-mbtiles/surrounding.mbtiles --minzoom=0 --maxzoom=14 --format=mbtiles --bbox="-3.2338,55.6082,-3.0326,55.7161" --scale=2.5 --metatile=15'
    return (createCentralTilesGlentress, createSurroundingTilesGlentress)

(createCentralTiles, createSurroundingTiles) = createInnersTileCreationCommands()
print os.system(createCentralTiles)
print os.system(createSurroundingTiles)


centralMbtilesFile = mbtilesDir + "central.mbtiles"
surroundingMbtilesFile = mbtilesDir + "surrounding.mbtiles"
centralTilesDir = "centralTiles"
centralTilesFullPathDir = mbtilesDir + centralTilesDir
surroundingTilesDir = "surroundingTiles"
surroundingTilesFullPathDir = mbtilesDir + surroundingTilesDir
finalMbtilesFile = mbtilesDir + "maptiles.mbtiles"
     

os.system("rm -rf " + surroundingTilesFullPathDir)
proc = subprocess.Popen(["/usr/local/bin/mb-util " +  centralMbtilesFile + " " + centralTilesFullPathDir  ], stdout=subprocess.PIPE, shell=True)
(out, err) = proc.communicate()
print "program output:", out, err
proc = subprocess.Popen(["/usr/local/bin/mb-util " +  surroundingMbtilesFile + " " + surroundingTilesFullPathDir  ], stdout=subprocess.PIPE, shell=True)
(out, err) = proc.communicate()
print "program output:", out, err
os.chdir(mbtilesDir)
os.system('rsync -a ' + centralTilesDir + '/ ' + surroundingTilesDir + '/')

proc = subprocess.Popen(["/usr/local/bin/mb-util " +  surroundingTilesFullPathDir + " " + finalMbtilesFile  ], stdout=subprocess.PIPE, shell=True)
(out, err) = proc.communicate()


