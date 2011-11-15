'''
Created on 2011/11/8

@author: hwangzong
'''
from math import sqrt as sqrt


class Distance():
    def __init__(self):
        pass
    
    def calc(self,list):
#       if not list:
        value=[]
        value2=[]
        p=0
        k=0
        while(p<len(list)):
            if(p%2==0):
                value.append(list[p])
            else:
                value2.append(list[p]) 
            p+=1       
        for x,y in zip(value,value2):
            k+=pow(x-y,2)
        return 1/(1+k) 
             
             
def main():
    list2 = [2.5,3.0,3.5,3.5,3.0,1.5,3.5,5.0,2.5,3.5,3.0,3.0]
    distance = Distance()
    q = distance.calc(list2)
    print 'the euclidean distance is "%s"' % q   
    return
        
        
if __name__ == '__main__':
    main()