'''
Created on 2013-5-3

@author: Simon@itechs
'''
edays = [["Short", 0, 4],
         ["Middle", 0, 0, 0, 4, 10, 20],
         ["Long", 0, 0, 10, 20]
         ]

def getMembershipValue(value, memfunc):
    count = 1
    isFlat = True
    begin = 1
    while (count < len(memfunc) and value > memfunc[count]):
        count += 1
        isFlat = not isFlat
        if (count % 2 != 0): begin = (begin + 1) % 2
    if (isFlat):
        return begin
    else:
        end = (begin + 1) % 2
        return float(begin) + float((end - begin) * (value - memfunc[count - 1])) / (memfunc[count] - memfunc[count - 1])
    
def getMembershipPair(value, memfuncs):
    result = ""
    for memfunc in memfuncs:
        tvalue = getMembershipValue(value, memfunc)
        if (tvalue > 0):
            result += "<%s, %.3f>" % (memfunc[0], tvalue)
    return result