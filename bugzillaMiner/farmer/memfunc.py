'''
Created on 2013-5-3

@author: Simon@itechs
'''
mf_edays = [["Short", 0, 1],
         ["Middle", 0, 0, 0, 1, 50, 58],
         ["Long", 0, 0, 50, 58]
         ]

mf_comments = [["Few", 1, 2],
         ["Middle", 0, 0, 1, 2, 4, 6],
         ["Many", 0, 0, 4, 6]
         ]

mf_modis = [["Few", 1, 2],
         ["Middle", 0, 0, 1, 2, 3, 5],
         ["Many", 0, 0, 3, 5]
         ]

mf_umodis = [["Few", 0, 1],
         ["Middle", 0, 0, 0, 1, 1, 3],
         ["Many", 0, 0, 1, 3]
         ]

labels = [["Transition", None],
          ["CommentNum", mf_comments],
          ["ElapseDays", mf_edays],          
          ["ModiNum", mf_modis],
          ["UniModiNum", mf_umodis]
          ]

def getMembershipValue(value, memfunc):
    count = 1
    isFlat = True
    begin = 1
    while (count < len(memfunc) and value >= memfunc[count]):
        count += 1
        isFlat = not isFlat
        if (count % 2 != 0): begin = (begin + 1) % 2
    if (isFlat):
        return begin
    else:
        end = (begin + 1) % 2
        return float(begin) + float((end - begin) * (value - memfunc[count - 1])) / (memfunc[count] - memfunc[count - 1])
    
def getMembershipPair(label, value, memfuncs):
    result = ""
    if (memfuncs == None):
        return "<%s_%s,%.2f> " % (value, label, 1)
    value = int(value)
    for memfunc in memfuncs:
        tvalue = getMembershipValue(value, memfunc)
        if (tvalue > 0):
            result += "<%s_%s,%.2f> " % (memfunc[0], label, tvalue)
    return result