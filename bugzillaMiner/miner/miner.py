'''
Created on 2013-3-6

@author: Simon@itechs
'''
import lxml.html
from statistician import *
from dataobject import *
from gl import *
import datetime
import time


from pyquery import PyQuery
from dateutil.parser import parse

global error_count        
global error_list
global filecount
global timestatis
global index

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

def record(timestatis, time, rtype):
    record = Record(time, rtype)
    timestatis.processRecord(record)
    
def processFile(filepath, timestatis):
    #print filepath
    try:
        fp = open(filepath, 'r')
        html = fp.read()
        fp.close()
        dom = lxml.html.fromstring(html)  
        title = getTitle(dom)
    #    print title
    #    if (not isHtmlValid(title)): return False
        
        reportStartTime = getReportStartTime(dom)
    #    print reportStartTime
        record(timestatis, reportStartTime, "reportStart")
        
        comments = getComments(dom)
        for comment in comments:
            record(timestatis, comment.time, "commentTime")
        return True
    except:
        global error_count
        global error_list
        error_count += 1
        error_list.append(filepath)
        return False
        
#    td = page('//*[@id="bz_show_bug_column_2"]/table/tbody/tr[1]/td[2]')
#    print td
    
def processHistoryFile(filepath, timestatis):
    try:
        fp = open(filepath, 'r')
        html = fp.read()
        fp.close()
        dom = lxml.html.fromstring(html)
        title = getTitle(dom)
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
#                content = getClearText(children[2].text_content())
                timestr = children[1].text_content().strip()
#                author = getClearText(children[0].text_content())
            else:
                pass
#                content = getClearText(children[0].text_content())
    #        print content
            if (timestr):
                record(timestatis, timestr, "reportModify")
    except:
        global error_count
        global error_list
        error_count = error_count + 1
        error_list.append(filepath)
        return False