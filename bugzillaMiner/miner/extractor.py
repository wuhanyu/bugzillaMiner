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

        #==================history==================
        modifications = commonFunc.getModifications(hdom)
        index = 0
        time = parse(reportStartTime)
        m_index = 0
        count = 1
        md_index = 0
        dcount = 1
        dtime = modifications[0].time
        for modi in modifications:
            if (modi.time > dtime):
                dcount += 1
                dtime = modi.time
            if (cmp(modi.content, "Status") == 0):
                line = ''
                line += modi.remove + '-' + modi.add + '\t'
                p = index 
                while (comments[p].time <= modi.time and p < len(comments) - 1):
                    p += 1
                line += str(p - index + 1) + '\t'
                index = p
                line += str(modi.time - time) + '\t'
                time = modi.time
                line += str(count - m_index - 1) + '\t'
                m_index = count
                line += str(dcount - md_index - 1) + '\t'
                md_index = dcount
                dtime = modi.time
                print line
            count += 1

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