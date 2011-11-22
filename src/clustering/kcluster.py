'''
Created on 2011/11/15

@author: ishida
'''
import random
import hcluster


def kcluster(rows,distance=hcluster.pearson,k=4):   
        ranges=[(min([row[i] for row in rows]),max([row[i] for row in rows]))
                for i in range(len(rows[0]))]
        
        clusters=[[random.random()*(ranges[i][1]-ranges[i][0])+ranges[i][0] 
                   for i in range(len(rows[0]))] for j in range(k)]
        
        lastmatches=None
        for t in range(100):
            print  'Iteration %d' % t
            bestmatches=[[]for i in range(k)]
             
            for j in range(len(rows)):
                 row = rows[j]
                 bestmatch=0
                 for i in range(k):
                     d=distance(clusters[i],row)
                     if d<distance(clusters[bestmatch],row):bestmatch=i
                 bestmatches[bestmatch].append(j)
 
            if bestmatches==lastmatches:break
            else:lastmatches=bestmatches
                     
            for i in range(k):
               avgs=[0.0]*len(rows[0])
               if len(bestmatches[i])>0:
                 for rowid in bestmatches[i]:
                     for m in range(len(rows[rowid])):
                         avgs[m]+=rows[rowid][m]
                 for j in range(len(avgs)):
                     avgs[j]/=len(bestmatches[i])
                 clusters[i]=avgs
    
        return bestmatches

                          
def main():
    blognames,words,data=hcluster.readfile('blogdata.txt')
    kclust=kcluster(data,k=10)
    print [blognames[r] for r in kclust[0]]
    print [blognames[r] for r in kclust[1]]
    print [blognames[r] for r in kclust[2]]
    print [blognames[r] for r in kclust[3]]
    print [blognames[r] for r in kclust[4]]
    print [blognames[r] for r in kclust[9]]
    print kclust
if __name__ == '__main__':
   main() 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
    
 
 

 
 
 
 
 
 

 
    
    