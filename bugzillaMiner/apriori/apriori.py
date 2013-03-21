"""
Description    : Simple Python implementation of the Apriori Algorithm
Author         : Abhinav Saini(abhi488@gmail.com)
Credits        : Cesare Zavattari(cesare@ctrl-z-bg.org) for making suggestions and refactoring code

Usage:
    $python apriori.py -f DATASET.csv -s minSupport  -c minConfidence
    
    Eg.
        $ python apriori.py -f DATASET.csv -s 0.15 -c 0.6

"""

from collections import defaultdict
from itertools import chain, combinations
from optparse import OptionParser
import re
import sys


def subsets(arr):
    """ Returns non empty subsets of arr"""
    return chain(*[combinations(arr, i + 1) for i, a in enumerate(arr)])


def returnItemsWithMinSupport(itemSet, transactionList, minSupport, freqSet):
    """calculates the support for items in the itemSet and returns a subset of the itemSet 
    each of whose elements satisfies the minimum support"""
    _itemSet = set()
    localSet = defaultdict(int)

    for item in itemSet:
        for transaction in transactionList:
            if item.issubset(transaction):
                freqSet[item]      += 1
                localSet[item]     += 1
    
    for item, count in localSet.items():
        support = float(count) / len(transactionList)
        
        if support >= minSupport:
            _itemSet.add(item)
    
    return _itemSet



def joinSet(itemSet, length):
    """Join a set with itself and returns the n-element itemsets"""
    return set([i.union(j) for i in itemSet for j in itemSet if len(i.union(j)) == length])


def getItemSetTransactionList(data_iterator):
    transactionList     = list()
    itemSet         = set()
    resultSet = set()
    for result, record in data_iterator:
        transaction = frozenset(record)
        transactionList.append(transaction)
        for item in transaction:
            itemSet.add(frozenset([item]))  # Generate 1-itemSets
        resultSet.add(frozenset([result]))
    return resultSet, itemSet, transactionList


def runApriori(data_iter, minSupport, minConfidence):
    """
    run the apriori algorithm. data_iter is a record iterator
    Return both: 
     - items (tuple, support)
     - rules ((pretuple, posttuple), confidence)
    """
    resultSet, itemSet, transactionList = getItemSetTransactionList(data_iter)
    
    freqSet         = defaultdict(int)
    largeSet         = dict()  # Global dictionary which stores (key=n-itemSets,value=support) which satisfy minSupport
    
    oneCSet         = returnItemsWithMinSupport(itemSet, transactionList, minSupport, freqSet)
    
    currentLSet     = oneCSet
    k = 2
    while(currentLSet != set([])):
        largeSet[k - 1]      = currentLSet
        currentLSet      = joinSet(currentLSet, k)
        currentCSet      = returnItemsWithMinSupport(currentLSet, transactionList, minSupport, freqSet)
        currentLSet      = currentCSet
        k = k + 1

    def getSupport(item):
            """local function which Returns the support of an item"""
            return float(freqSet[item]) / len(transactionList)

    toRetItems = []
    for key, value in largeSet.items():
        toRetItems.extend([(tuple(item), getSupport(item)) 
                           for item in value])

    toRetRules = []
    for key, value in largeSet.items()[1:]:
        for item in value:
            for element in resultSet:
                if (item.issuperset(element) == True):
                    remain = item.difference(element)
                    if (len(remain) > 0):
                        support = getSupport(item)
                        confidence = support / getSupport(remain)
                        if confidence >= minConfidence:
                            toRetRules.append(((tuple(remain), tuple(element)),
                                               confidence, support))
    return toRetItems, toRetRules


def printResults(items, rules):
    """prints the generated itemsets and the confidence rules"""
    for item, support in items:
        print "item: %s , %.3f" % (str(item), support)
    print "\n------------------------ RULES:"
    rules = reversed(sorted(sorted(rules, key=lambda element : element[2]), key=lambda element : element[1]))
    resultCount = {}
    for rule, confidence, support in rules:
        pre, post = rule
        if (not resultCount.has_key(post)):
            resultCount[post] = 0
        resultCount[post] += 1
        if (resultCount[post]) > 3: continue
        print "Rule: %s ==> %s , Support: %.3f, Confidence: %.3f" % (str(pre)[:-2] + ")", str(post)[1:-2], support, confidence)


def dataFromFile(fname):
    """Function which reads from the file and yields a generator"""
    file_iter = open(fname, 'rU')
    for line in file_iter:
        line = line.strip().rstrip(',')  # Remove trailing comma
        tmplist = line.split(',')
        record = frozenset(tmplist)
        result = tmplist[0]
        yield result, record



if __name__ == "__main__":

    optparser = OptionParser()
    optparser.add_option('-f', '--inputFile', dest='input', help='the filename which contains the comma separated values', default=None)
    optparser.add_option('-s', '--minSupport', dest='minS', help='minimum support value', default=0.15, type='float')
    optparser.add_option('-c', '--minConfidence', dest='minC', help='minimum confidence value', default=0.6, type='float')

    (options, args) = optparser.parse_args()

    inFile = None
    if options.input is None:
        inFile = sys.stdin
    elif options.input is not None:
        inFile = dataFromFile(options.input)
    else:
        print 'No dataset filename specified, system with exit\n'
        sys.exit('System will exit')

    minSupport         = options.minS
    minConfidence      = options.minC
    items, rules     = runApriori(inFile, minSupport, minConfidence)

    printResults(items, rules)
