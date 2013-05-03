'''
Created on 2013-5-3

@author: Simon@itechs
'''
import random

if __name__ == '__main__':
    filename = r"../result/SequenceDataExctractor_2013-03-16 1423.txt"
    fin = open(filename, 'r')
    data = fin.read()
    fin.close()
    linecount = data.count('\n')
    MAX_SELECT = 10000
    factor = float(MAX_SELECT) / linecount
    samplelist = sorted(random.sample(range(0, linecount), MAX_SELECT))
    i = 0
    fin = open(filename, 'r')
    count = 0
    foutname = fin.name.replace(".txt", "-s" + str(MAX_SELECT) + ".txt")
    fout = open(foutname, "w")
    for line in fin:
        if (i >= MAX_SELECT): break
        if (count == samplelist[i]):
            i += 1
            fout.write(line)
        count += 1
    fin.close()
    fout.close()
    
    
        