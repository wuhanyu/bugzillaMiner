'''
Created on 2013-3-12

@author: Simon
'''
import commonFunc
from dateutil.relativedelta import *
from dataobject import *

class SequenceExtractor(object):
    def __init__(self):
        pass
    
    def processFile(self, dom, hdom):
        reportStartTime = commonFunc.getReportStartTime(dom)
    #    print reportStartTime
        
        comments = commonFunc.getComments(dom)
        for comment in comments:
            print comment
            
        pass
        #==================history==================
        modifications = commonFunc.getModifications(hdom)
        for modi in modifications:
            print str(modi)
        pass
    
    def __str__(self):
        result = ''
        return result
    
    def outputCount(self, filepath):
        file_object = open(filepath, 'w')    
        file_object.close()
        return


class Sample(object):
    def __init__(self):
        pass
    
    def processFile(self, dom, hdom):
        pass
    
    def __str__(self):
        result = ''
        return result
    
    def outputCount(self, filepath):
        file_object = open(filepath, 'w')    
        file_object.close()
        return