'''
Created on 2013-3-6

@author: Simon@itechs
'''
from miner import *
import datetime
error_count = 0
error_list = []
filecount = 1
timestatis = TimeStatistician()

if __name__ == '__main__':
    starttime = datetime.datetime.now()
#    src = '/media/DATA/mozilla.bugs/'
#    src = 'D:\\mozilla.bugs\\'
    src = 'D:\\sample\\'
   # print src
    

    begin = 240000
    end = 252450
    filecount = 1
    flag = True
    for i in range(begin, end):
 #        print '*' * 40
        
        filename = src + str(i) + '.html'
        if (flag):
            print filename + '\t(' + str(filecount) + ')'
            flag = False
        
        if (processFile(filename, timestatis)):
            pass    
            history_file = gethistoryName(filename)
            processHistoryFile(history_file, timestatis)
            filecount = filecount + 1
            flag = True
    print timestatis
    timestatis.outputCount('../result/count.txt')
    endtime = datetime.datetime.now()
    print (endtime - starttime)
