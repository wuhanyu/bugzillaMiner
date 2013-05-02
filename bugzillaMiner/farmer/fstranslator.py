'''
Created on 2013-5-2

@author: Simon@itechs
'''

def getEDaysQ(days):
    if (days < 2):
        return 1, 0, 0
    elif (days < 10):
        return 

if __name__ == '__main__':
    input = open('../result/TransitionExctractor_2013-05-02 1542.txt', 'r')
    for line in input:
        print line