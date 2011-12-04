'''
Created on 2011/11/22

@author:hatless
Begin from demo,change something in the demo,and try that,observe anything wrong
or anything out

let's start my job from crawling webs.
u should pay attention to something that below:
1.
2
3





'''
import urllib2  
from BeautifulSoup import BeautifulSoup  
from urlparse import urljoin
import re
from db import connection

ignorewords = {'the':1, 'of':1, 'to':1, 'and':1, 'a':1, 'in':1, 'is':1, 'it':1}
index_urls = {}

class crawler: 
   
  def __init__(self):
    pass  
    
  def crawl(self, pages, depth=2):
    for i in range(depth):
      newpages = {}
      for page in pages:
        try:
          c = urllib2.urlopen(page)
        except:
          print "Could not open %s" % page
          continue
        try:
          soup = BeautifulSoup(c.read())
#          self.addtoindex(page,soup)#be careful for this step
          words = self.separatewords(self.gettextonly(soup))
          links = soup('a')
          urls = []
          linkTexts = []
          for link in links:
            if ('href' in dict(link.attrs)):
              url = urljoin(page, link['href'])
              if url.find("'") != -1: continue
              url = url.split('#')[0]  # remove location portion
              if url[0:4] == 'http' and not self.isindexed(url):
                self.setindexs(url)
                newpages[url] = 1 
                urls.append(url)           
                linkText = self.gettitleonly(link)  #first step
                linkTexts.append(self.cutwords(len(urls) - 1, linkText))
          self.addlinkref(page, urls, linkTexts, words)#save to mongodb
        except:
          print "Could not parse page %s" % page

      pages = newpages
      
 
  def gettextonly(self, soup):
    resulttext = ''
    list = soup('p') 
    for p in list: 
        v = p.string
        if v == None:  
          resulttext += self.gettext(p)
        else: 
          resulttext += v.strip()
    return resulttext    
     
#   # Extract the text from an HTML page (no tags)
  def gettext(self, p): 
      v = p.string
      resulttext = ''
      if v == None:
          c = p.contents     
          for t in c:
            subtext = self.gettext(t)
            resulttext += subtext + '\n'
          return resulttext 
      else:
          return v.strip()  
    
  
  
 # Extract the text from an HTML page (no tags)
  def gettitleonly(self, soup):
    v = soup.string
    if v == None:   
      c = soup.contents     
      resulttext = ''
      for t in c:
        subtext = self.gettextonly(t)
        resulttext += subtext + '\n'
      return resulttext
    else:
      return v.strip()  
#  
  # input str 
  # output disc,demo:{'words': [{'word': 'aaa'}, {'word': 'bbb'}, {'word': 'ccc'}, {'word': 'ddd'}]}  
  # Seperate the words by any non-whitespace character  
  def separatewords(self, text):
    splitter = re.compile('\\W*')
    links = []
    for s in splitter.split(text):
        if s != '' and s.lower() not in ignorewords:
            links.append(s.lower())
    return links

  def cutwords(self, directary, text):
    splitter = re.compile('\\W*')
    words = []
    for s in splitter.split(text):
        if s != '' and s.lower() not in ignorewords:
           words.append({'word':s.lower(), "directary":directary})
    return {'pair':words}

  def addlinkref(self, urlFrom, urls, linkTexts, words):  
    fromid = self.getUrlid('urlFrom', urlFrom)#got url origin web
    if fromid != None: return 
    return connection.insert(urlFrom=urlFrom, urls=urls, words=words, linkTexts=linkTexts)
    
#   
  def getUrlid(self, field, value):
     return connection.selectII(field=value)    
  
  # Return true if this url is already indexed
  def isindexed(self, url):
    if url in index_urls:
        return True
    else:
        return False

  def setindexs(self, url):
    index_urls[url] = 1
    

def main():
    cr = crawler()
    cr.crawl(['http://kiwitobes.com/wiki/Categorical_list_of_programming_languages.html'])

if __name__ == '__main__':
    main()
   
   
   
   
   
#c=urllib2.urlopen('http://member.zebo.com/Main?event_key=USERSEARCH&wiowiw=wiw&keyword=car&page=%d')
#soup=BeautifulSoup(c.read())
#links=soup('a')
#print links[10]
#print links[10]['href']
#if __name__ == '__main__':
#    pass
      
#def tanamoto(v1,v2):
#  c1,c2,shr=0,0,0
#  
#  for i in range(len(v1)):
#    if v1[i]!=0: c1+=1 # in v1
#    if v2[i]!=0: c2+=1 # in v2
#    if v1[i]!=0 and v2[i]!=0: shr+=1 # in both
#  
#  return 1.0-(float(shr)/(c1+c2-shr))
#
#
#wants,people,data=hcluster.readfile('zebo.txt')
#clust=hcluster.hcluster(data, distance=tanamoto)
#hcluster.drawdendrogram(clust, wants)




