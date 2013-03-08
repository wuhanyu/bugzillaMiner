'''
Created on 2013-3-6

@author: Simon@itechs
'''
import lxml.html
from statistician import *
from dataobject import *
import datetime
import threading
import time

from pyquery import PyQuery
from dateutil.parser import parse

def gethistoryName(filename):
    return filename[:-5] + '-history.html'

def isHtmlValid(title):
    if (cmp(title, 'Access Denied') == 0): return False
    else: return True

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
        dom = None
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
        error_count = error_count + 1
        error_list.append(filepath)
        return False
        
#    td = page('//*[@id="bz_show_bug_column_2"]/table/tbody/tr[1]/td[2]')
#    print td
    
def processHistoryFile(filepath, timestatis):
    try:
        fp = open(filepath, 'r')
        html = fp.read()
        fp.close()
        dom = None
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

class Miner(threading.Thread):
    def __init__(self, begin, end, N):
        threading.Thread.__init__(self)
        self.begin = begin
        self.end = end
        self.N = N

    def run(self):
        global filecount
        global timestatis
        global index
#        i = self.begin
#        for i in range(self.begin, self.end):
        while (index < self.end):
     #        print '*' * 40
            filename = src + str(index) + '.html'
            index = index + 1
            if (filecount % 100 == 0):
                print filename + '\t(' + str(filecount) + ')'
            
            if (processFile(filename, timestatis)):
                pass    
                history_file = gethistoryName(filename)
                processHistoryFile(history_file, timestatis)
                filecount = filecount + 1
  
global error_count        
global error_list
global filecount
global timestatis
global index

if __name__ == '__main__':
    starttime = datetime.datetime.now()

    src = 'D:\\mozilla.bugs\\'
#    src = 'D:\\sample\\'
    print src
    timestatis = TimeStatistician()
    
#    processFile(files[0], ts)
#    history_file = gethistoryName(files[0])
#    processHistoryFile(history_file, ts)
    error_count = 0
    error_list = []
    filecount = 1
    begin = 000000
    end = 600000
    miners = []
    N = 16
    index = 0
    for i in range(0, N):
#        miners.append(Miner(begin + (end-begin) / N * i, begin + (end-begin) / N * (i + 1)))
        miners.append(Miner(begin, end, N))
        miners[i].start()
    
    flag = True
    while (flag):
        flag = False
        number = 0
        for miner in miners:
            if (miner.is_alive()):
                flag = True
                number = number + 1
        print number
        time.sleep(10)

#    filecount = 1
#    for i in range(000000, 600000):
# #        print '*' * 40
#        filename = src + str(i) + '.html'
#        if (filecount % 100 == 0):
#            print filename + '\t(' + str(filecount) + ')'
#        
#        if (processFile(filename, timestatis)):
#            pass    
#            history_file = gethistoryName(filename)
#            processHistoryFile(history_file, timestatis)
#            filecount = filecount + 1
    print timestatis
    timestatis.outputCount('../result/count.txt')
    endtime = datetime.datetime.now()
    print (endtime - starttime)