'''
Created on 2013-3-6

@author: Simon@itechs
'''
from miner import *
import datetime
from gl import *

DEBUG = True
if __name__ == '__main__':
    '''
    Test script for the miner
    '''
    starttime = datetime.datetime.now()
#    src = '/media/DATA/mozilla.bugs/'
#    src = 'D:\\mozilla.bugs.test\\'
    src = 'D:\\sample\\'
   # print src
    processor = getProcessorFromTaskType(TASK_TYPE)

    begin = 240000
    end = 252450
    begin = 248115
    end = begin + 1
    filecount = 1
    flag = True
    for i in range(begin, end):
 #        print '*' * 40
        
        filename = src + str(i) + '.html'
        if (flag):
            print filename + '\t(' + str(filecount) + ')'
            flag = False
        
        if (processFile(filename, processor)):  
            history_file = gethistoryName(filename)
            processHistoryFile(history_file, processor)
            filecount = filecount + 1
            flag = True
    print processor
    output(processor)
    endtime = datetime.datetime.now()
    print (endtime - starttime)
    global error_list
    print error_list
