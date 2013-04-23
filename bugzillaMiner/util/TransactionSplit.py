'''
Created on 2013-4-13

@author: Simon@itechs
'''
import fileinput

if __name__ == '__main__':
    outputs = {}
    input = open('../data.csv.arff', 'r')
    head = ''
    for line in input:
        if (cmp(line, '@data\n') != 0):
            head += line
        else:
            head += line
            break
        tmp = line.split(' ')
        if (len(tmp) > 1 and cmp(tmp[1], 'Transition') == 0):
            outputfiles = tmp[2][1:-2].split(',')
            for otf in outputfiles:
                outputs[otf] = open('../data/'+otf + '.arff', 'w')
            print outputfiles
    for output in outputs:
        outputs[output].write(head)
    for line in input:
        tmp = line.split(',')
        outputs[tmp[1]].write(line)
    for output in outputs:
        outputs[output].close()
