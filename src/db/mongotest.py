'''
Created on 2011/12/1

@author: ishida
'''
import pymongo 
import random
import string
import os

conn = pymongo.Connection('localhost', 27017)
db = conn['perform']
coll = db['test']
testdata = []
def init_testdata():
    for i in xrange(1000):
        s1 = ''.join([random.choice(string.hexdigits) for j in xrange(16)])
        s2 = ''.join([random.choice(string.letters) for j in xrange(200)])
        testdata.append((s1, s2))

def insert_mongo():
    for s1, s2 in testdata: coll.insert({'_id': s1, 'content': s2})
def find_mongo():
    for s1, s2 in testdata:
        s = coll.find_one({'_id': s1})
def testfunc(funcname, times=1000):
    from timeit import Timer
    t = Timer("%s()" % funcname, "from __main__ import *")
    print 'funcname: %s used %f' % (funcname, t.timeit(times) / times)
if __name__ == '__main__':
    # os.fork()
    os.fork()
    init_testdata()
    testfunc('insert_mongo', times=100)
    testfunc('find_mongo', times=100)
