'''
Created on 2013-3-12

@author: Simon
'''

class SequenceExtractor(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''


class Sample(object):
    def __init__(self):
        pass
    
    def processFile(self, dom):
        pass
    
    def processHistoryFile(self, dom):
        pass
    
    def __str__(self):
        result = ''
        return result
    
    def outputCount(self, filepath):
        file_object = open(filepath, 'w')    
        file_object.close()
        return