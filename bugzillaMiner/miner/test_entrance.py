'''
Created on 2013-3-6

@author: Simon@itechs
'''
from miner import *
import datetime
import gl
from commonFunc import *

if __name__ == '__main__':
    gl.DEBUG = True
    '''
    Test script for the miner
    '''
    starttime = datetime.datetime.now()
#    src = '/media/DATA/mozilla.bugs/'
#    src = 'D:\\mozilla.bugs.test\\'
    src = 'D:\\sample\\'
#    print src
    processor = getProcessorFromTaskType(gl.TASK_TYPE)

    begin = 240000
    end = 252450
#    begin = 248115
#    end = begin + 1
    filecount = 1
    for i in range(begin, end):
 #        print '*' * 40
        
        filename = src + str(i) + '.html'
        
        if (processFile(filename, processor)):  
            filecount = filecount + 1
            print filename + '\t(' + str(filecount) + ')'
    print processor
    
    output(processor)
    endtime = datetime.datetime.now()
    print (endtime - starttime)
    print gl.error_list
