'''
Created on 19 Jan 2015

@author: murrayking
'''
import re


duffRecordName = "/records//duffRen/ame"
operationOver = "/records//addddd/sdfsd"

old = "/records//?([^/]*)$"
newreg = "/records//?(.*?)/$"
recordName = re.findall(old, duffRecordName)
print recordName
if "/" in recordName:
    print 'remove trailing /'
    print "and escape here"
    
 # Check POST/PUT.GET
operation = re.findall("/records//?[^/]+/[^/]+$",operationOver)
print operation
 # It is an operation over a record asset




 # Path has subdirectories error
