'''
Created on 1 Jan 2015

@author: murray
'''
import re
import sys


colorred = '501400FF'
colorblue = '50F03214'
colorblack = '50000000'

#Find all coordinates
with open('/home/murray/map-mobile/app/src/main/assets/black-route.kml') as fp:
    cords = ''
    for line in fp:
        m = re.search("<coordinates>(.*?)</coordinates>", line)
        if m:
            cords += m.groups()[0] + ','
            
        
kmlbody =''' <?xml version="1.0" encoding="utf-8" ?>
<kml xmlns="http://www.opengis.net/kml/2.2">
<Document id="root_doc">
<Schema name="green_route" id="green_route">
    <SimpleField name="id" type="int"></SimpleField>
</Schema>
<Folder><name>green_route</name>
  <Placemark>
    <Style><LineStyle><color>{color}</color><width>14</width></LineStyle><PolyStyle><fill>0</fill></PolyStyle></Style>
    <ExtendedData><SchemaData schemaUrl="#green_route">
        <SimpleData name="id">2</SimpleData>
    </SchemaData></ExtendedData>
      <LineString><altitudeMode>relativeToGround</altitudeMode><coordinates>{co}</coordinates></LineString>
  </Placemark>

</Folder>
</Document></kml>'''  

kmlbody =kmlbody.format(co=cords, color=colorblack)
print kmlbody