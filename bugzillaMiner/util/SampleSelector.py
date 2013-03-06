'''
Created on 2013-3-6

@author: Simon@itechs
'''
import os
import shutil

if __name__ == '__main__':
    #===========================================================================
    # for root,dirs,files in os.walk('D:/mozilla.bugs'):
    #===========================================================================
    src = 'D:/mozilla.bugs/'
    dst = 'D:/mozilla.bugs.test/'
    print src
    print dst + str(1) + '/'
    for root,dirs,files in os.walk(src):
        for index in range(1,6):
            base = 1000000 * index
            offset = 6000
            for i in range(base, base + offset):
                print files[i]
                shutil.copy(src + files[i], dst + str(i) + '/' + files[i]) 
