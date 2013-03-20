#!/usr/bin/env python
# -*- coding: utf-8 -*- 
'''
Created on 2013-3-12

@author: Simon
'''

import commonFunc
import gl
from dateutil.relativedelta import *
from dataobject import *

class SequenceExtractor(object):
    IS_FINAL_OUTPUT = False
    def __init__(self):
        pass
    
    def getSequence(self, modifications):
        line = ''
        status = None
        for modi in modifications:
            if (cmp(modi.content, "Status") == 0):
                if (not status):
                    line += "NEW"
                    status = "NEW"
                if (status and cmp(modi.remove, status) == 0):
                    line += '-' + modi.add
                else:
                    line += '-' + modi.remove + '-' + modi.add
                status = modi.add

        return line
    
    def getCountBeforeTime(self, list, time, isUnique=False):
        count = 0
        if (not isUnique):
            for item in list:
                if (item.time < time): count += 1
                else: break
        else:
            timeindex = list[0].time
            count = 1
            for item in list:
                if (item.time < time):
                    if (item.time > timeindex):
                        count += 1
                        timeindex = item.time
                else:
                    break
        return count
    
    def processFile(self, dom, hdom, output=None):
        reportStartTime = commonFunc.getReportStartTime(dom)
    #    print reportStartTime
        comments = commonFunc.getComments(dom)
        title = commonFunc.getTitle(dom).split(u' – ')[0][4:]
        
        #==================history==================
        modifications = commonFunc.getModifications(hdom)
        
        line = self.getSequence(modifications)
        if (len(line) > 0):
            reportStartTime = commonFunc.getReportStartTime(dom)
            start_time = parse(reportStartTime)
            index = -1
            while (cmp(modifications[index].content, "Status") != 0):
                index -= 1
            end_time = modifications[index].time
            elapsed_days = (end_time - start_time).days
            elapsed_comments = self.getCountBeforeTime(comments, end_time)
            elapsed_modifications = self.getCountBeforeTime(modifications, end_time)
            elapsed_unique_modifications = self.getCountBeforeTime(modifications, end_time, True)
            line += '\t' + str(elapsed_days) + '\t' + str(elapsed_comments)
            line += '\t' + str(elapsed_modifications)
            line += '\t' + str(elapsed_unique_modifications)
        if (gl.DEBUG): print line
        if (output):
            output.writelines([title + '\t' + line + '\n'])
        pass
    
    def __str__(self):
        result = ''
        return result
    
    def outputCount(self, filepath):
        file_object = open(filepath, 'w')    
        file_object.close()
        return

class TransitionExtractor(object):
    IS_FINAL_OUTPUT = False
    def __init__(self):
        pass
    
    def processFile(self, dom, hdom, output=None):
        reportStartTime = commonFunc.getReportStartTime(dom)
    #    print reportStartTime
        comments = commonFunc.getComments(dom)
        title = commonFunc.getTitle(dom).split(u' – ')[0][4:]

        #==================history==================
        modifications = commonFunc.getModifications(hdom)
        index = 0
        time = parse(reportStartTime)
        m_index = 0
        count = 1
        md_index = 0
        dcount = 1
        dtime = modifications[0].time
        tmplines = []
        for modi in modifications:
            if (modi.time > dtime):
                dcount += 1
                dtime = modi.time
            if (cmp(modi.content, "Status") == 0):
                line = ''
                line += modi.remove + '-' + modi.add + '\t'
                p = index 
                while (len(comments) > 0 and comments[p].time <= modi.time and p < len(comments) - 1):
                    p += 1
                line += str(p - index + 1) + '\t'
                index = p
                line += str((modi.time - time).days) + '\t'
                time = modi.time
                line += str(count - m_index - 1) + '\t'
                m_index = count
                line += str(dcount - md_index - 1) + '\t'
                md_index = dcount
                dtime = modi.time
#                print line
                tmplines.append(title + '\t' + line + '\n')
            count += 1
        if (output):
            output.writelines(tmplines)
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