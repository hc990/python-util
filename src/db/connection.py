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
        c = Connection(host="localhost", port=27017)
        print "connected successfully"
    except ConnectionFailure, e:
        sys.stderr.write("Conld not connect to MongoDB: %s" % e)
        sys.exit(1)
    return c['mydb']

c = connect()
#
def insert(**pros):
    return c.page.insert(pros, safe=True)

#def selectI(field,value):
#    c = connect()
#    return c.pages.find_one({field:value})

def selectII(**values):
    return c.page.find_one(values)  

def selectI(*values):
    return c.page.find_one(values)

def select(values):
    return c.page.find_one(values)

def selectEntrys(values):
    return c.page.find(values)

def selectcount(value):
    return c.page.find(value).count()

def creatindex():
    c.page.create_index("urlFrom", background=True, unique=True, drop_dups=True)


def main():
#    creatindex()
#    insert(url='title1', words=["word ab", "word2 bc"], links=[{'link':"cd"}, {'link':"ef"}])
#    insert(url='title2', words=["word gh", "word qq"], links=[{'link':"sm"}, {'link':"killer"}])
#    insert(url='title3', words=["word3 if", 'word4 as'], links=[{'link':"sb"}, {'link':"hate"}])
#    print selectII(title='title2', words={'word':9}, links={'link':11})  
     print selectcount('')

if __name__ == '__main__':
    print c.page.find({"urls":{"$in":["http://kiwitobes.com/wiki/2002.html"]}}).count()
#    c.page.update({"urlFrom":'http://kiwitobes.com/wiki/Categorical_list_of_programming_languages.html'}, {"$push":{"urls":"http://kiwitobes.com/wiki/2002.html"}}, multi=True, safe=True)
#    main()
