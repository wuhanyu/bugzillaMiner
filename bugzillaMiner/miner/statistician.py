'''
Created on 2013-3-7

@author: Simon
'''

from commonFunc import *
from dateutil.relativedelta import *

class TimeStatistician(object):
    '''
    Statistic for the information displayed in time sequences
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
    
    def __str__(self):
        result = '-'*20 + 'Begin' + '-'*20 + '\n'
        result = result + 'Begin At : ' + str(self.beginTime) + '\n'
        result = result + 'End At : ' + str(self.endTime) + '\n'
        for dictname in self.countDict:
            result = result + dictname + '  ' + str(self.countDict[dictname]) + '\n'
        result = result + '-'*20 + 'Finish' + '-'*20 + '\n'
        return result
        
    def outputCount(self, filepath):
        file_object = open(filepath, 'w')    
        for dictname in self.countDict:
            list = []
            list.append(dictname + ':\n')
            time = self.beginTime
            while (time < self.endTime):
                timestr = getTimeStr(time)
                if (self.countDict[dictname].has_key(timestr)):
                    list.append(timestr + '\t' + str(self.countDict[dictname][timestr]) + '\n')
                else:
                    list.append(timestr + '\t0\n')
                time = time + relativedelta(months=+1)
            file_object.writelines(list)
        file_object.close()
        
class SequenceStatistician(object):
    def __init__(self):
        pass