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
    
def processFile(filepath, processor, output=None):
    #print filepath
    try:
        history_filepath = gethistoryName(filepath)
        dom = getDomOfFile(filepath)
        hdom = getDomOfFile(history_filepath)
        title = getTitle(dom)
        
    #    print title
        if (output):
            processor.processFile(dom, hdom, output)
        else:
            processor.processFile(dom, hdom)
        return True
    except IOError:
        pass
    except IndexError:
        stitle = title.encode('utf-8').strip()
        print stitle
        if (gl.DEBUG and cmp(stitle, "Access Denied") != 0): raise
    except:
        errorHandle(filepath)
        return False