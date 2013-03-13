'''
Created on 2013-3-6

@author: Simon@itechs
'''

from statistician import *
from dataobject import *
import datetime
import time


from pyquery import PyQuery
from dateutil.parser import parse
    
def processFile(filepath, processor):
    #print filepath
    try:
        dom = getDomOfFile(filepath)
        title = getTitle(dom)
    #    print title
    #    if (not isHtmlValid(title)): return False
        processor.processFile(dom)
        return True
    except IOError:
        pass
    except:
        errorHandle(filepath)
        return False
        
#    td = page('//*[@id="bz_show_bug_column_2"]/table/tbody/tr[1]/td[2]')
#    print td
    
def processHistoryFile(filepath, processor):
    try:
        dom = getDomOfFile(filepath)
        processor.processHistoryFile(dom)
        return True
    except IOError:
        pass
    except:
        errorHandle(filepath)
        return False