'''
Created on 2011/11/12

@author: ishida
'''
from PIL import Image,ImageDraw   

class DrawDrogram(object):  
    '''  
    classdocs
    '''
    def __init__(self):
        pass  
        '''
        Constructor
        ''' 
    def drawdendrogram(self,jpeg='aaa.jpg'):
        img=Image.new('RGB',(200,200),(255,255,255))
        draw=ImageDraw.Draw(img)
        draw.line((0,0,200,200),fill=(100,100,100))
        img.save(jpeg,'Png')
        
    
    
def main():
   drawDrogram=DrawDrogram()
   drawDrogram.drawdendrogram()

if __name__ == '__main__':
   main()