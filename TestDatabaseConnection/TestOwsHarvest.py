'''
Created on 12 Jan 2015

@author: murrayking
from owslib.csw import CatalogueServiceWeb
>>> csw = CatalogueServiceWeb('http://geodiscover.cgdi.ca/wes/serviceManagerCSW/csw')
>>> csw.identification.type
'''

datagov = 'http://csw.data.gov.uk/geonetwork/srv/en/csw'
inspireportal = 'http://inspire-geoportal.ec.europa.eu/GeoportalProxyWebServices/resources/OGCCSW202/AT?service=CSW&version=2.0.2&request=GetCapabilities'
localhost = 'http://localhost:8000/?service=CSW'
gogeo = 'http://gogeo-at.edina.ac.uk/geonetwork/srv/en/csw?request=GetCapabilities&version=2.0.2&service=CSW'
scotsdi = 'http://scotgovsdi.edina.ac.uk/geonetwork/srv/en/csw?request=GetCapabilities&version=2.0.2&service=CSW'

# from owslib.csw import CatalogueServiceWeb
# csw = CatalogueServiceWeb(datagov, version='2.0.2')
# print(csw.identification.type)
# csw.getrecords(keywords=['birds','fowl'], maxrecords=20)
# print csw.results
# 
# for rec in csw.records:
#     print csw.records[rec].title
# print csw.results
# csw.getrecords(bbox=[-179, -77, 180, 80], maxrecords=20, startposition=10)
# for rec in csw.records:
#     print csw.records[rec].title

from owslib.csw import CatalogueServiceWeb
import os
recobjs = []  # records
pagesize=10

# if init raises error, this might not be a CSW
csw = CatalogueServiceWeb(gogeo, timeout=60)

outPutDir = "/Users/murrayking/Documents/Gogeo2"

# get all supported typenames of metadata
# so we can harvest the entire CSW

# try for ISO, settle for Dublin Core
csw_typenames = 'csw:Record'
csw_outputschema = 'http://www.opengis.net/cat/csw/2.0.2'

grop = csw.get_operation_by_name('GetRecords')
if all(['gmd:MD_Metadata' in grop.parameters['typeNames']['values'],
        'http://www.isotc211.org/2005/gmd' in grop.parameters['outputSchema']['values']]):
    csw_typenames = 'gmd:MD_Metadata'
    csw_outputschema = 'http://www.isotc211.org/2005/gmd'


# now get all records
# get total number of records to loop against

try:
    csw.getrecords2(typenames=csw_typenames, resulttype='hits',
                   outputschema=csw_outputschema)
    matches = csw.results['matches']
except:  # this is a CSW, but server rejects query
    raise RuntimeError(csw.response)

if pagesize > matches:
    pagesize = matches



def makeGetRecordsCall(csw, csw_typenames, r, pagesize, csw_outputschema):
    def getrecords2():
        return csw.getrecords2(typenames=csw_typenames, startposition=r,
                       maxrecords=pagesize, outputschema=csw_outputschema, esn='full')
    return getrecords2

failureStartAtRecord=22611
# loop over all catalogue records incrementally
for r in range(failureStartAtRecord, matches+1, pagesize):
    
    getrecords = makeGetRecordsCall(csw, csw_typenames, r, pagesize, csw_outputschema)
    try:
        getrecords()
    except Exception, err:  # this is a CSW, but server rejects query
        #retry again just incase
        try: 
            getrecords()
        except Exception, err:
            getrecords()  # this is a CSW, but server rejects query
    for k, v in csw.records.iteritems():
        if csw_typenames == 'gmd:MD_Metadata':
            print(v.xml)
            
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            fn = outPutDir + "/" + k +".xml"
            dn = os.path.dirname(fn)
            if not os.path.exists(dn):
                os.makedirs(dn)
            print(fn)
            print("Number of records" + str(r))
            with open(fn, "w") as text_file:
                text_file.write(v.xml)
        else:
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print("NOt iso record ignore")
