'''
Created on 2013-3-7

@author: Simon
'''

from commonFunc import *
from dataobject import *
from dateutil.relativedelta import *

class TimeStatistician(object):
    '''
    Statistic for the information displayed in time sequences
    '''
    countDict = {}
    beginTime = None
    endTime = None

    def __init__(self):
        pass
        
    def processFile(self, dom):
        reportStartTime = getReportStartTime(dom)
    #    print reportStartTime
        self.processRecord(Record(reportStartTime, "reportStart"))
        
        comments = getComments(dom)
        for comment in comments:
            print comment
            self.processRecord(Record(comment.time, "commentTime"))
        pass
    
    def processHistoryFile(self, dom):       
        modifications = getModifications(dom)
        for modi in modifications:
#            print str(modi)
            if (modi.time):
                self.processRecord(Record(modi.time, "reportModify"))
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
    

        
class SequenceStatistician(object):
    countDict = {}
    def __init__(self):
        pass
    
    def processFile(self, dom):
        pass
    
    def processHistoryFile(self, dom):
        pass
    
    def __str__(self):
        result = ''
        return result
    
    def outputCount(self, filepath):
        file_object = open(filepath, 'w')    
        for dictname in self.countDict:
            list = []
            list.append(dictname + ':\n')
            time = self.beginTime
            while (time < self.endTime):
                timestr = getTimeStrYear(time)
                if (self.countDict[dictname].has_key(timestr)):
                    list.append(timestr + '\t' + str(self.countDict[dictname][timestr]) + '\n')
                else:
                    list.append(timestr + '\t0\n')
                time = time + relativedelta(months=+1)
            file_object.writelines(list)
        file_object.close()