'''
Created on 2013-3-6

@author: Simon@itechs
'''
from miner import *
import datetime
import threading

class Miner(threading.Thread):
    def __init__(self, begin, end, N, src):
        threading.Thread.__init__(self)
        self.begin = begin
        self.end = end
        self.N = N
        self.src = src

    def run(self):
        global filecount
        global timestatis
        global index
#        i = self.begin
#        for i in range(self.begin, self.end):
        while (index < self.end):
#        print '*' * 40
            filename = self.src + str(index) + '.html'
            index = index + 1
            if (filecount % 100 == 0):
                print filename + '    (' + str(filecount) + ')   ' + str(datetime.datetime.now())
            
            if (processFile(filename, timestatis)):
                pass    
                history_file = gethistoryName(filename)
                processHistoryFile(history_file, timestatis)
                filecount = filecount + 1

timestatis = TimeStatistician()
error_count = 0
error_list = []
filecount = 1
index = 0

if __name__ == '__main__':
    starttime = datetime.datetime.now()
#    src = '/media/DATA/mozilla.bugs/'
    src = 'D:\\mozilla.bugs.test\\'
#    src = 'D:\\sample\\'

    begin = 000000
    end = 600000
    miners = []
    N = 16
    index = begin
    for i in range(0, N):
        miners.append(Miner(begin, end, N, src))
        miners[i].start()
    
    flag = True
    while (flag):
        flag = False
        number = 0
        for miner in miners:
            if (miner.is_alive()):
                flag = True
                number = number + 1
        print number
        time.sleep(10)
    print timestatis
    timestatis.outputCount('../result/count.txt')
    endtime = datetime.datetime.now()
    print (endtime - starttime)
