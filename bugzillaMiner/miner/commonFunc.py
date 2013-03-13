'''
Created on 2013-3-8

@author: Simon@itechs
'''
import datetime
import statistician
import lxml.html
import sys
from gl import *
from dataobject import *


def getTimeStr(time):
    timestr = str(time)[:7]
    return timestr

def gethistoryName(filename):
    return filename[:-5] + '-history.html'

def output(processor):
    OUTPUT_PATH = '../result/' + TASK_TYPE + '_' + str(datetime.datetime.now()).replace(":", '')[0:15] + '.txt'
    print OUTPUT_PATH
    processor.outputCount(OUTPUT_PATH)
    
def getProcessorFromTaskType(TASK_TYPE):
    processor = None
    if (cmp(TASK_TYPE, "TimeStatistic")==0):
        processor = statistician.TimeStatistician()
    elif (cmp(TASK_TYPE, "SequenceStatistic")==0):
        processor = statistician.SequenceStatistician()
    elif (cmp(TASK_TYPE, "SequenceExctractor")==0):
        pass
    else:
        print "Task type error, no task type '" + TASK_TYPE + "' found"
        exit(1)
    return processor

def getClearText(tmpstr):
    return tmpstr.strip().replace('\n              ', '; ').replace(' ', '_')

def getReportStartTime(dom):
    items = dom.xpath('//*[@id="bz_show_bug_column_2"]/table/tr[1]/td[2]')
    return items[0].text[:-4]

def getComments(dom):
    authors = dom.xpath('//*[@id="comments"]/div/div/span/span[@class="vcard"]')[1:]
    times = dom.xpath('//*[@id="comments"]/div/div/span[@class="bz_comment_time"]')[1:]
    result = []
    i = 0
    for time in times:
#        print time.text.strip()
#        print authors[i].text_content().strip()
        result.append(Comment(authors[i].text_content().strip(), time.text.strip()))
        i = i + 1
    return result
    
def getTitle(dom):
    title = dom.xpath('//title')[0].text
    return title

def getDomOfFile(filepath):
    fp = open(filepath, 'r')
    html = fp.read()
    fp.close()
    dom = lxml.html.fromstring(html)
    return dom

def errorHandle(filepath):
    global error_count
    global error_list
    print "Unexpected error:", sys.exc_info()
    error_count += 1
    error_list.append(filepath)