'''
Created on 31 Jan 2015

@author: murray
'''

import xml.etree.ElementTree as ET
root = ET.parse("/home/murray/testkml.kml")
result = ''

for e in root.findall('./Document/Folder/Placemark'):
    # How to make decisions based on attributes even in 2.6:
    print 'name'
    name = e.find("name")
    if name is not None:
        print name.text
    linestring = e.find("LineString/coordinates");
    print linestring.text
    if e.attrib.get('name') == 'foo':
        result = e.text
        break
  
    
