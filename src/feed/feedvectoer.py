'''
Created on 2011/11/10

@author: ishida
'''
import feedparser as fp
import re
import urllib
    
class Feedvector():   
      def getwordcounts(self,url):
        d=fp.parse(url)
        wc={}
        for e in d.entries:
          if 'summary' in e:
              summary=e.summary
          else:
              summary=e.description
          words = self.getwords(e.title+' '+summary)
          for word in words:  
           wc.setdefault(word,0)
           wc[word]+=1
        return d.feed.title,wc
    
      def getwords(self,html):
        txt=re.compile(r'<[^>]+>').sub('',html)
        words=re.compile(r'[^A-Z^a-z]+').split(txt)
        print words
        return [word.lower() for word in words if word!='']
       
      def __init__(self):
           pass
  
def webread():
   webfile = urllib.urlopen("http://kiwitobes.com/clusters/feedlist.txt")
   return webfile
  
def main():
   apcount={}
   wordcounts={}
   feedvector=Feedvector()
   webfile = webread().read()
   feedlist =[line for line in webfile]
   print feedlist
   for feedurl in feedlist:
       title,wc=feedvector.getwordcounts(feedurl)
       for word,count in wc.items():
           apcount.setdefault(word,0)
           if count > 1:
              apcount[word]+=1
   wordlist=[]
   for w,bc in apcount.items():
       frac  = float(bc)/len(feedlist)
       if frac>0.1 and frac<0.5:wordlist.append(w)     
   out=file('aa.txt','w')
   out.write('blog')
   for word in wordlist:out.write('\t%s' % word)
   out.write('\n')
   for blog,wc in wordcounts.items():
      out.write(blog)
      for word in wordlist:
           if word in wc:
               out.write('\t%s' % wc[word])
           else:out.write('\t0')
      out.write('\n')

    
if __name__ == '__main__':
   main()
     