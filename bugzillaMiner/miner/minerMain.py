'''
Created on 2013-3-6

@author: Simon@itechs
'''
import os
import glob
import lxml.html
from statistician import *
from dataobject import *

from pyquery import PyQuery
from dateutil.parser import parse

def gethistoryName(filename):
    return filename[:-5] + '-history.html'

def isHtmlValid(title):
    if (cmp(title, 'Access Denied') == 0): return False
    else: return True

def getClearText(str):
    return str.strip().replace('\n              ', '; ').replace(' ', '_')

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
    
def getTitle(page):
    title = page('title').text()
    return title

def record(timestatis, time, rtype):
    record = Record(time, rtype)
    timestatis.processRecord(record)
    
def processFile(filepath, timestatis):
    #print filepath
    html = open(filepath, 'r').read()
    dom = lxml.html.fromstring(html)
    page = PyQuery(html)
    title = getTitle(page)
    
#    print title
    if (not isHtmlValid(title)): return False
    
    reportStartTime = getReportStartTime(dom)
#    print reportStartTime
    record(timestatis, reportStartTime, "reportStart")
    
    comments = getComments(dom)
    for comment in comments:
        record(timestatis, comment.time, "commentTime")

    return True
#    td = page('//*[@id="bz_show_bug_column_2"]/table/tbody/tr[1]/td[2]')
#    print td
    
def processHistoryFile(filepath, timestatis):
    html = open(filepath, 'r').read()
    dom = lxml.html.fromstring(html)
    page = PyQuery(html)
    title = getTitle(page)
#    print title
    
    items = dom.xpath('//*[@id="bugzilla-body"]/table/tr')
#    print (items[0].text.strip())
#    for item in items:
#        print item
    for item in items[1:]:
        children = item.getchildren()
        author = None
        timestr = None
        if (len(children) == 5):
#            print children[0].text.strip() + '*' * 6
            content = getClearText(children[2].text_content())
            timestr = children[1].text_content().strip()
            author = getClearText(children[0].text_content())
        else:
            content = getClearText(children[0].text_content())
#        print content
        if (timestr):
            record(timestatis, timestr, "reportModify")
            
                 
if __name__ == '__main__':
    src = 'D:\\mozilla.bugs.test\\'
#    src = 'D:\\sample\\'
    print src
    files = glob.glob(src + '*[0-9].html')
    ts = TimeStatistician()
    
#    processFile(files[0], ts)
#    history_file = gethistoryName(files[0])
#    processHistoryFile(history_file, ts)
    filecount = 1
    for filename in files:
#        print '*' * 40
        print filename + '\t(' + str(filecount) + ')'
        filecount = filecount + 1
        if (processFile(filename, ts)):
            pass    
            history_file = gethistoryName(filename)
            processHistoryFile(history_file, ts)

    print ts
    ts.outputCount('../result/count.txt')