'''
Created on 2013-3-8

@author: Simon@itechs
'''
import datetime
import statistician
from gl import *

def getTimeStr(time):
    timestr = str(time)[:7]
    return timestr

def gethistoryName(filename):
    return filename[:-5] + '-history.html'

def output(processor):
    OUTPUT_PATH = '../result/' + TASK_TYPE + '_' + str(datetime.datetime.now()).replace(":", '')[0:15] + '.txt'
    print OUTPUT_PATH
    processor.outputCount(OUTPUT_PATH)
    
def getProcessorFromTaskType(TASK_TYPE):
    processor = None
    if (cmp(TASK_TYPE, "TimeStatistic")==0):
        processor = statistician.TimeStatistician()
    elif (cmp(TASK_TYPE, "SequenceStatistic")==0):
        pass
    elif (cmp(TASK_TYPE, "SequenceExctractor")==0):
        pass
    else:
        print "Task type error, no task type '" + TASK_TYPE + "' found"
        exit(1)
    return processor