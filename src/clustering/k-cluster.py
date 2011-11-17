'''
Created on 2011/11/15

@author: ishida
'''
def kcluster(rows,distance=pearson):
    ranges=[(min([row[i] for row in rows]),max([row[i] for row in rows]))
            for i in range(len(row[0]))]
    clusters=[[random.random()*(ranges[i][1]-ranges[i][0])+ranges[i][0] for i in range(len(row[0]))] for j in range(k)]