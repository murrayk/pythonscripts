'''
Created on 1 Mar 2015

@author: murray
'''

import os
from os.path import expanduser
home = expanduser("~")

import subprocess


dirwithmbtiles = home + "/mergembtiles"
hiresmbtiles = dirwithmbtiles + "/innersldwide.mbtiles"
lowressurrounding = dirwithmbtiles + "/innersld.mbtiles"
tileDirectoryHiRes = dirwithmbtiles + "/tiles"
tileDirectoryLowRes = dirwithmbtiles + "/tilesl"
finalMbtiles = dirwithmbtiles + "/finalOutput.mbtiles"

os.system("rm -rf " + tileDirectoryHiRes )
os.system("rm -rf " + tileDirectoryLowRes)
proc = subprocess.Popen(["mb-util " +  hiresmbtiles + " " + tileDirectoryHiRes  ], stdout=subprocess.PIPE, shell=True)
(out, err) = proc.communicate()
print "program output:", out, err
proc = subprocess.Popen(["mb-util " +  lowressurrounding + " " + tileDirectoryLowRes  ], stdout=subprocess.PIPE, shell=True)
(out, err) = proc.communicate()
print "program output:", out, err
os.chdir(dirwithmbtiles)
os.system("rsync -a tiles/ tilesl/ ")

proc = subprocess.Popen(["mb-util " +  tileDirectoryLowRes + " " + finalMbtiles  ], stdout=subprocess.PIPE, shell=True)
(out, err) = proc.communicate()


