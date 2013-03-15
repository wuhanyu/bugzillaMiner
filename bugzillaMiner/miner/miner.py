'''
Created on 2013-3-6

@author: Simon@itechs
'''


from dataobject import *
from commonFunc import *
import datetime
import time


from pyquery import PyQuery
from dateutil.parser import parse
    
def processFile(filepath, processor):
    #print filepath
    try:
        history_filepath = gethistoryName(filepath)
        dom = getDomOfFile(filepath)
        hdom = getDomOfFile(history_filepath)
        title = getTitle(dom)
        
    #    print title
        processor.processFile(dom, hdom)
        return True
    except IOError:
        pass
    except:
        errorHandle(filepath)
        return False