'''
Created on 2011/11/12

@author: ishida
'''

class docRead(object):
    '''
    classdocs
    '''


    def __init__(self):
        pass
        '''
        Constructor
        '''
    def readfile(self,filename):
        file=open(filename)
        lines = [line for line in file]
        colnames = lines[0].strip('\t')[1:]
        rownames=[]
        data=[]
        for line in lines[1:]:
            p=line.strip().split('\t')
            rownames.append(p[0])
            data.append([float(x) for x in p[1:]])
        return rownames,colnames,data
    
def main():
    docRead=docRead()  
    blognames,words,data=docRead.readfile('blogdata.txt')        
    print blognames
    print words

if __name__ == '__main__':
    main()