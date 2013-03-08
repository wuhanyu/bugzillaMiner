'''
Created on 2013-3-7

@author: Simon
'''
from dateutil.parser import parse
def getTimeStr(time):
    timestr = str(time)[:7]
    print timestr
    return timestr

class Record(object):
    time = None
    recordtypeetype = None
    content = None
    def __init__(self, timestr, recordtype):
        if (timestr != None):
            time = parse(timestr)
            self.time = time
        if (recordtype != None):
            self.recordtype = recordtype

class TimeStatistician(object):
    '''
    classdocs
    '''
    timeSeq = []
    countDict = {}
    beginTime = None
    endTime = None

    def __init__(self):
        timeSeq = []
        
    def renewBound(self, record):
        if (self.beginTime == None):
            self.beginTime = record.time
            self.endTime = record.time
        elif (record.time < self.beginTime):
            self.beginTime = record.time
        elif (record.time > self.endTime):
            self.endTime = record.time
            
        
    def countRecord(self, record):
        recordtype = record.recordtype
        if (not self.countDict.has_key(recordtype)):
            self.countDict[recordtype] = {}
        timestr = getTimeStr(record.time)
        if (self.countDict[recordtype].has_key(timestr)):
            self.countDict[recordtype][timestr] = self.countDict[recordtype][timestr] + 1
        else:
            self.countDict[recordtype][timestr] = 1
        return
    
    def processRecord(self, record):
        self.renewBound(record)
        self.countRecord(record)
        pass