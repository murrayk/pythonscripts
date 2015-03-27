'''
Created on 4 Dec 2014

@author: murrayking
'''

import requests
import sqlite3
import re
import glob
import os.path

def readMbtileDBAndWriteToFiles():
    conn = sqlite3.connect('/home/murray/glentressfull.mbtiles')
    with conn:
    
        conn.row_factory = sqlite3.Row
       
        cur = conn.cursor() 
        cur.execute("SELECT * FROM tiles")

        rows = cur.fetchall()

        ext = ".png"
        for row in rows:
            (z,x,y) = (row["zoom_level"], row["tile_column"], row["tile_row"])
            ymax = 1 << z;
            invertedY = ymax - y -1;
            tileName =  "z%sx%sy%s" % (z,x,invertedY)
            print tileName
            tileName = tileName + ext
            tileName = "/home/murray/temp-tiles/" + tileName
            with open(tileName, 'wb') as output_file:
                output_file.write(row["tile_data"])
                
            #uploadToDataStore(tileName);
    

def uploadTiles():

    files = glob.glob("/home/murray/temp-tiles/*png") 
    for f in files:
        uploadToDataStore(f)
    

def uploadToDataStore(tileName):
    #r = requests.get('http://google.com')
    #unicode.capitalize()
    print tileName
    url = 'http://praxis-cab-89616.appspot.com/index.jsp'
    #url = 'http://localhost:8888/index.jsp'
    txtParsePostUrl = requests.get(url)
    match = re.search(r'action="(.*?)"', txtParsePostUrl.text)
# If-statement after search() tests if it succeeded
    postUrl = None
    if match:                      
        postUrl = match.group(1) ## 'found word:cat'
    else:
        print 'did not find'
        
    files = {'file': (os.path.basename(tileName), open(tileName, 'rb'), 'image/png')}
        
    
    r = requests.post(postUrl, files=files)
    
    
#readMbtileDBAndWriteToFiles()

uploadTiles()
