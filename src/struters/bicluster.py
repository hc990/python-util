'''
Created on 2011/11/18

@author: ishida
'''
class bicluster:
    
    def __init__(self,vec,left=None,right=None,distance=0.0,id=None):
        self.left=left
        self.right=right
        self.vec=vec
        self.id=id
        self.distance=distance
        
        
        