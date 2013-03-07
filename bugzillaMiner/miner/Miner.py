'''
Created on 2013-3-6

@author: Simon@itechs
'''
import glob
import lxml.html

from pyquery import PyQuery

def gethistoryName(filename):
    return filename[:-5] + '-history.html'

def isHtmlValid(title):
    if (cmp(title, 'Access Denied') == 0): return False
    else: return True

def getClearText(s):
    return s.strip().replace('\n              ', '; ').replace(' ', '_')

def processFile(filepath):
    #print filepath
    html = open(filepath, 'r').read()
    dom = lxml.html.fromstring(html)
    page = PyQuery(html)
    title = page('title').text()
    
#    print title
    if (not isHtmlValid(title)): return False
    
    items = dom.xpath('//*[@id="bz_show_bug_column_2"]/table/tr[1]/td[2]')
#    print items[0].text

    return True
#    td = page('//*[@id="bz_show_bug_column_2"]/table/tbody/tr[1]/td[2]')
#    print td
    
def processHistoryFile(filepath):
    html = open(filepath, 'r').read()
    dom = lxml.html.fromstring(html)
    page = PyQuery(html)
    title = page('title').text()
    print title
    
    items = dom.xpath('//*[@id="bugzilla-body"]/table/tr')
#    print (items[0].text.strip())
#    for item in items:
#        print item
    for item in items[1:]:
        children = item.getchildren()
        if (len(children) == 5):
#            print children[0].text.strip() + '*' * 6
            print getClearText(children[2].text_content())
        else:
            print getClearText(children[0].text_content())
                 
if __name__ == '__main__':
    src = 'D:\\mozilla.bugs.test\\'
    print src
    files = glob.glob(src + '*[0-9].html')
    
#    processFile(files[0])
#    history_file = gethistoryName(files[0])
#    processHistoryFile(history_file)
    
    for filename in files:
        print '*' * 40
#        print filename
        if (processFile(filename)):    
            history_file = gethistoryName(filename)
            processHistoryFile(history_file)