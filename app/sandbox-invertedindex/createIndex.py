'''
Author: Arden Dertat
Contact: ardendertat@gmail.com
License: MIT License
'''

#!/usr/bin/env python

import sys
import re
from porterStemmer import PorterStemmer
from collections import defaultdict
from array import array
import gc
import hashlib

porter=PorterStemmer()

class CreateIndex:

    def __init__(self):
        self.index=defaultdict(list)    #the inverted index

    
    def getStopwords(self):
        '''get stopwords from the stopwords file'''
        f=open(self.stopwordsFile, 'r')
        stopwords=[line.rstrip() for line in f]
        self.sw=dict.fromkeys(stopwords)
        f.close()
        

    def getTerms(self, line):
        '''given a stream of text, get the terms from the text'''
        line=line.lower()
        line=re.sub(r'[^a-z0-9 ]',' ',line) #put spaces instead of non-alphanumeric characters
        line=line.split()
        line=[x for x in line if x not in self.sw]  #eliminate the stopwords
        #line=[ porter.stem(word, 0, len(word)-1) for word in line] #stems all terms, doubles processing time
            #not sure if this stemming is appropriate for this application
        #return hashlib.sha224(line).hexdigest()
        return line


    def parseCollection(self):
        ''' returns the id, title and text of the next page in the collection '''
        doc=[]
        for line in self.collFile:
            if line=='</page>\n':
                break
            doc.append(line)
        
        curPage=''.join(doc)
        pageid=re.search('<id>(.*?)</id>', curPage, re.DOTALL)
        pagetitle=re.search('<title>(.*?)</title>', curPage, re.DOTALL)
        pagetext=re.search('<text>(.*?)</text>', curPage, re.DOTALL)
        
        if pageid==None or pagetitle==None or pagetext==None:
            return {}

        d={}
        d['id']=pageid.group(1)
        d['title']=pagetitle.group(1)
        d['text']=pagetext.group(1)

        return d


    def writeIndexToFile(self):
        '''write the inverted index to the file'''
        f=open(self.indexFile, 'w')
        for term in self.index.iterkeys():
            postinglist=[]
            for p in self.index[term]:
                docID=p[0]
                positions=p[1]
                postinglist.append(':'.join([str(docID) ,','.join(map(str,positions))]))
            #term = hashlib.sha512(term).hexdigest()   #enocdes all terms in SHA512 hash
            print >> f, ''.join((term,'|',';'.join(postinglist)))
            
        f.close()
        

    def getParams(self):
        '''get the parameters stopwords file, collection file, and the output index file'''
        param=sys.argv
        self.stopwordsFile=param[1]
        self.collectionFile=param[2]
        self.indexFile=param[3]
        

    def createIndex(self):
        '''main of the program, creates the index'''
        self.getParams()
        self.collFile=open(self.collectionFile,'r')
        self.getStopwords()
                
        #bug in python garbage collector!
        #appending to list becomes O(N) instead of O(1) as the size grows if gc is enabled.
        gc.disable()
        
        pagedict={}
        pagedict=self.parseCollection()
        #main loop creating the index
        while pagedict != {}:                    
            lines='\n'.join((pagedict['title'],pagedict['text']))
            pageid=int(pagedict['id'])
            terms=self.getTerms(lines)
            
            #build the index for the current page
            termdictPage={}
            for position, term in enumerate(terms):
                try:
                    termdictPage[term][1].append(position)
                except:
                    termdictPage[term]=[pageid, array('I',[position])]
            
            #merge the current page index with the main index
            for termpage, postingpage in termdictPage.iteritems():
                self.index[termpage].append(postingpage)
            
            pagedict=self.parseCollection()


        gc.enable()
            
        self.writeIndexToFile()
        
    
if __name__=="__main__":
    c=CreateIndex()
    c.createIndex()
    

