'''
Created on 2013-3-8

@author: Simon@itechs
'''
import datetime
import statistician
import extractor
import lxml.html
import sys
import gl
from dataobject import *

def getTimeStr(time):
    timestr = str(time)[:7]
    return timestr

def getTimeStrYear(time):
    timestr = str(time)[:4]
    return timestr

def gethistoryName(filename):
    return filename[:-5] + '-history.html'

def getOutputFilepath(TASK_TYPE):
    return '../result/' + TASK_TYPE + '_' + str(datetime.datetime.now()).replace(":", '')[0:15] + '.txt'

def getOutput(processor):
    if (processor.IS_FINAL_OUTPUT):
        return None
    else:
        return open(getOutputFilepath(gl.TASK_TYPE), 'w')

def output(processor):
    if (not processor.IS_FINAL_OUTPUT):
        return 
    OUTPUT_PATH = getOutputFilepath(gl.TASK_TYPE)
    print OUTPUT_PATH
    processor.outputCount(OUTPUT_PATH)
    
def getProcessorFromTaskType(TASK_TYPE):
    processor = None
    if (cmp(TASK_TYPE, "TimeStatistic")==0):
        processor = statistician.TimeStatistician()
    elif (cmp(TASK_TYPE, "SequenceStatistic")==0):
        processor = statistician.SequenceStatistician()
    elif (cmp(TASK_TYPE, "SequenceExctractor")==0):
        processor = extractor.SequenceExtractor()
    elif (cmp(TASK_TYPE, "SequenceDataExctractor")==0):
        processor = extractor.SequenceDataExtractor()
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
    contents = dom.xpath('//*[@id="comments"]/div/pre[@class="bz_comment_text"]')[1:]
    result = []
    i = 0
#    print len(authors), len(times), len(contents)
    for time in times:
#        print time.text.strip()
#        print authors[i].text_content().strip()
        author = authors[i].text_content().strip()
        timestr = time.text.strip()
        content = contents[i].text_content().strip()
        result.append(Comment(author, timestr, content))
        i = i + 1
    return result

def getModifications(dom):
    result = []
    items = dom.xpath('//*[@id="bugzilla-body"]/table/tr')

    for item in items[1:]:
        children = item.getchildren()
        if (len(children) == 5):
            add = getClearText(children[4].text_content())
            remove = getClearText(children[3].text_content())
            content = getClearText(children[2].text_content())
            timestr = children[1].text_content().strip()
            author = getClearText(children[0].text_content())
        else:
            add = getClearText(children[2].text_content())
            remove = getClearText(children[1].text_content())
            content = getClearText(children[0].text_content())
        result.append(Modification(author, timestr, content, remove, add))
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
    print "Unexpected error:", sys.exc_info()
    gl.error_count += 1
    gl.error_list.append(filepath)
    if (gl.DEBUG):
        raise