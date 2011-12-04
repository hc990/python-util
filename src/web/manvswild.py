'''
Created on 2011/12/1

@author: hatemyself
'''
from db import connection
import string



class manvswild: 

    def query(self, word):
        basewords = word.split(' ')
        entrys = self.gotwordpairs(basewords)
        scores = self.getscoredlist(basewords, entrys)
        rankedscores = [(score, url) for (url, score) in scores.items()]
        rankedscores.sort()
        rankedscores.reverse()
        for (score, url) in rankedscores[0:10]:
          print '%f\t%s' % (score, url)
        return basewords, [r[1] for r in rankedscores[0:10]]
    
    #get values from table
    def gotwordpairs(self, basewords):  
        entrys = [entry for entry in connection.selectEntrys({'words':{"$in":basewords}})]    
        return entrys
                
    #how many words in the one row
    def getscoredlist(self, basewords, entrys):    
        totalscores = dict([(entry.get('urlFrom'), 0) for entry in entrys]) 
        weights = [
                 (1.0, self.frequencyscore(basewords, entrys)),
                 (0.1, self.locationscore(basewords, entrys)), (0.1, self.inboundlinkscore(basewords, entrys))
                 ]
        
        for (weight, scores) in weights:
          for url in totalscores:
            totalscores[url] += weight * scores[url]
    
        return totalscores
    
    def normalizescores(self, scores, smallIsBetter=0):
        vsmall = 0.00001 # Avoid division by zero errors
        if smallIsBetter:
          minscore = min(scores.values())
          return dict([(u, float(minscore) / max(vsmall, l)) for (u, l) in scores.items()])
        else:
          maxscore = max(scores.values())
          if maxscore == 0: maxscore = vsmall
          return dict([(u, float(c) / maxscore) for (u, c) in scores.items()])
    
    def locationscore(self, basewords, entrys):
#        locations = dict([(row[0], 1000000) for row in rows])
        locations = dict([(entry.get('urlFrom'), 1000000) for entry in entrys]) 
        loc = 0
        for entry in entrys:
            urlFrom = entry.get('urlFrom')
            words = entry.get('words')
            for baseword in basewords:
               loc = loc + words.index(baseword,)
        if loc < locations[urlFrom]: locations[urlFrom] = loc
        
        return self.normalizescores(locations, smallIsBetter=1)
    
    def frequencyscore(self, basewords, entrys):
        totalscores = dict([(entry.get('urlFrom'), 0) for entry in entrys]) 
        for entry in entrys:
            urlFrom = entry.get('urlFrom')
            words = entry.get('words')
            for word in words:
                if word.lower() in basewords:
                   totalscores[urlFrom] += 1
        return self.normalizescores(totalscores)
    
    def inboundlinkscore(self, basewords, entrys):
        uniqueurls = dict([(entry.get('urlFrom'), 1) for entry in entrys])
        inboundcount = dict([(u, connection.selectcount({"urls":{"$in":[u]}})) for u in uniqueurls])   
        print inboundcount
        return self.normalizescores(inboundcount)

if __name__ == '__main__':
       manvswild().query("java")
