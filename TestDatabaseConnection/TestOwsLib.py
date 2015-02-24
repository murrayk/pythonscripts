from owslib.wms import WebMapService
wms = WebMapService('http://localhost:8000/?service=CSW&version=2.0.2&request=GetCapabilities', version='2.0.2')
print(wms.identification.type)

