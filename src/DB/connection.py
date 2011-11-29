'''
Created on 2011/10/18

@author: ishida
'''
import sys

from pymongo import Connection  
from pymongo.errors import ConnectionFailure


"""connect to MongoDB"""
def connect():
    try:
        c = Connection(host="localhost",port=27017)
        print "connected successfully"
    except ConnectionFailure, e:
        sys.stderr.write("Conld not connect to MongoDB: %s" % e)
        sys.exit(1)
    return c['mydb']


#
def insert(**pros):
    c=connect()
    return c.pages.insert(pros,safe=True)

#def selectI(field,value):
#    c = connect()
#    return c.pages.find_one({field:value})

def selectII(**values):
    c = connect()
    return c.pages.find_one(values)

def main():    
    insert(url='title1',words=[{'word':5},{'word':'6'}],links=[{'link':7},{'link':8}])
#    insert('words','links','title',title='title2',words=[{'word':9},{'word':10}],links=[{'link':11},{'link':12}])
#    insert('words','links','title',title='title3',words=[{'word':15},{'word':'16'}],links=[{'link':17},{'link':18}])
    print selectII(title='title2',words={'word':9},links={'link':11})  


if __name__ == '__main__':
    main()