'''
Created on 2013-5-2

@author: Simon@itechs
'''
import memfunc

if __name__ == '__main__':
    finname = '../result/TransitionExctractor_2013-05-02 1542.txt'
    fin = open(finname, 'r')
    foutname = fin.name.replace(".txt", "-fs.txt")
    fout = open(foutname, 'w')
    for line in fin:
        tmp = line.split("\t")
        outputline = ''
        tmp = tmp[2:6]
        for i, item in enumerate(tmp):
            outputline += memfunc.getMembershipPair(memfunc.labels[i][0], int(item), memfunc.labels[i][1])
        fout.write(outputline[:-1] + "\n")
    fin.close()
    fout.close()