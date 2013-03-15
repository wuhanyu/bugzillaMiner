'''
Created on 2013-3-6

@author: Simon@itechs
'''
from miner import *
import gl
from commonFunc import *
import datetime
import threading

class Miner(threading.Thread):
    '''
    Each Class Miner has an independent tread
    '''
    def __init__(self, begin, end, N, src, processor):
        threading.Thread.__init__(self)
        self.begin = begin
        self.end = end
        self.N = N
        self.src = src
        self.processor = processor

    def run(self):
#        i = self.begin
#        for i in range(self.begin, self.end):
        while (gl.index < self.end):
#        print '*' * 40
            filename = self.src + str(gl.index) + '.html'
            gl.index = gl.index + 1
            if (gl.filecount % 100 == 0):
                print filename + '    (' + str(gl.filecount) + ')   ' + str(datetime.datetime.now())
            
            if (processFile(filename, self.processor)):
                pass    
                gl.filecount = gl.filecount + 1
           
if __name__ == '__main__':
    gl.DEBUG = False
    '''
    Main script for the miner, optimized by multi-threading tech
    '''
    starttime = datetime.datetime.now()
#    src = '/media/DATA/mozilla.bugs/'
    src = 'D:\\mozilla.bugs.test\\'
#    src = 'D:\\sample\\'
    processor = getProcessorFromTaskType(gl.TASK_TYPE)
    begin = 000000
    end = 600000
    miners = []
    N = 16
    gl.index = begin
    for i in range(0, N):
        miners.append(Miner(begin, end, N, src, processor))
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
    print processor
    output(processor)
    endtime = datetime.datetime.now()
    print (endtime - starttime)
