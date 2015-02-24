'''
Created on 31 Jan 2015

@author: murray
'''
import re
import xml.etree.ElementTree as ET

from os.path import expanduser
home = expanduser("~")

#IMPORTANT remove xmlns from kml files 
baseDir = home + '/map-mobile/app/src/main/assets/'
blueroute = [baseDir + "blue-route.kml","blue_loc_names","blue_loc_coords"]
redroute = [baseDir + "red-route.kml","red_loc_names","red_loc_coords"]
testredroute = [baseDir + "test-red-route.kml","red_loc_names","red_loc_coords"]
blackroute = [baseDir + "black-route.kml","black_loc_names","black_loc_coords"]
testblackroute = [baseDir + "test-black-route.kml","black_loc_names","black_loc_coords"]
innersBaseDir = home + '/map-mobile/app/src/inners/assets/'
redrouteinners = [ innersBaseDir + "innersxc.kml","red_inners_loc_names","red_innersloc_coords"]
route = redrouteinners
names = []
coords = []
root = ET.parse(route[0])
def printOutXml(myid, els):
    print '<string-array name="{0}">'.format(myid)
    for e in els:
        print '<item>{0}</item>'.format(e)
    print '</string-array>'


for e in root.findall('./Document/Folder/Placemark'):
    # How to make decisions based on attributes even in 2.6:


    name = e.find("ExtendedData/SchemaData/SimpleData[@name='routelabel']")
    if name is not None:
        names.append(name.text)
        linestring = e.find("LineString/coordinates");
        match = re.match('^[-+]?[0-9]*\.?[0-9]+.[-+]?[0-9]*\.?[0-9]+', linestring.text)
    
        coords.append( match.group(0))

printOutXml(route[1], names)
printOutXml(route[2], coords)
  