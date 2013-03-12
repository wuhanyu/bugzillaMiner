'''
Created on 2013-3-8

@author: Simon@itechs
'''
from dateutil.parser import parse
import types

class Comment(object):
    '''
    Data jam for Comment Object, each is a comment posted by a DEV
    '''
    author = None
    time = None
    def __init__(self, author, timestr):
        if (author):
            self.author = author
        if (timestr):
            time = parse(timestr)
            self.time = time
        pass
        '''
        Constructor
        '''

class Record(object):
    '''
    Data jam for an modifying action made by core DEV
    '''
    time = None
    recordtypeetype = None
    content = None
    def __init__(self, timestr, recordtype):
        if (timestr):
            if (type(timestr) is types.StringType):
                time = parse(timestr)
                self.time = time
            else:
                self.time = timestr
        if (recordtype):
            self.recordtype = recordtype       