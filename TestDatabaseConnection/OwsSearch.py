'''
Created on 13 Jan 2015

@author: murrayking
'''
from owslib.csw import CatalogueServiceWeb
datagov = 'http://csw.data.gov.uk/geonetwork/srv/en/csw'
inspireportal = 'http://inspire-geoportal.ec.europa.eu/GeoportalProxyWebServices/resources/OGCCSW202/AT?service=CSW&version=2.0.2&request=GetCapabilities'
localhost = 'http://localhost:8000/?service=CSW'

# from owslib.csw import CatalogueServiceWeb
# 
# print(csw.identification.type)
# csw.getrecords2(keywords=['birds','fowl'], maxrecords=20)
# print csw.results
# 
# for rec in csw.records:
#     print csw.records[rec].title
# print csw.results
# csw.getrecords(bbox=[-179, -77, 180, 80], maxrecords=20, startposition=10)
# for rec in csw.records:
#     print csw.records[rec].title

csw = CatalogueServiceWeb(datagov, version='2.0.2')
from owslib.csw import CatalogueServiceWeb
import os
recobjs = []  # records


from owslib.fes import PropertyIsEqualTo, PropertyIsLike, BBox
birds_query = PropertyIsEqualTo('csw:AnyText', 'tree')
csw.getrecords2(constraints=[birds_query], maxrecords=20, outputschema='http://www.isotc211.org/2005/gmd')
print csw.results
for k, v in csw.records.iteritems():
    print(v.xml)

