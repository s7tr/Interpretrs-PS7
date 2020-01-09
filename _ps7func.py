# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 22:42:57 2020

@author: SaurabhX360
"""

def edgeinit(self):
    self.matrixlength=len(self.vertices)
    self.edges=[[None for i in range(self.matrixlength)] for j in range(self.matrixlength)]
    
    for i in range(self.matrixlength):
        for j in range(self.matrixlength):
            self.edges[i][j]='.'
    
def edgebuilder(self):
    
    print(self.vertices)
    cKey= -1
    lKey= -1
    for i in range(len(self.parseline)):
        candidate = self.parseline[i][0]
        cKey=self.findCandidateKey(candidate)
        print(self.parseline[i],candidate,'.', cKey)
        for language in self.uniqueLang:
            if language in self.parseline[i][1:]:
                lKey=self.findLanguageKey(language)
                print(candidate, language,'.', cKey, lKey)
                self.edges[cKey][lKey] = 1
                self.edges[lKey][cKey] = 1
            else:
                lKey=-1
        cKey=-1
    
                
def findCandidateKey(self,candidate):
    for i in range(len(self.vertices)):
        if self.vertices[i]==candidate:
            break
    return i
    
def findLanguageKey(self,language):
    keyisfound = False
    for i in range(len(self.vertices)):
        if self.vertices[i]==language:
            keyisfound=True
            break
    if keyisfound is True:
        return i
    else:
        return -1

            
def uniqueCandidates(self):
    self.uniqueCand=[]
    for pline in self.parseline:
        plinecand = pline[0]
        if plinecand not in self.uniqueCand:
            self.uniqueCand.append(plinecand)
    return self.uniqueCand

def uniqueLanguages(self):
    self.uniqueLang=[]
    for pline in self.parseline:
        plinelang = pline[1:]
        for lang in plinelang:
            if lang not in self.uniqueLang:
                self.uniqueLang.append(lang)                    
    return self.uniqueLang

def createvertices(self):
    for cand in self.uniqueCand:
        self.vertices.append(cand)
    for lang in self.uniqueLang:
        self.vertices.append(lang)
    print(self.vertices)
   

def removeCovLang(self,ck,tbcl):
    candKey = ck
    tobeCovLang = tbcl
    
    for l in range(len(self.uniqueCand), self.matrixlength):
        if (self.edges[candKey][l] == 1):
            
            print(candKey, l)
            tobeCovLang = tobeCovLang[:l] + tobeCovLang[l+1:]
    return(tobeCovLang)
    
def getInterpreterRank(self):
    
    interpreterRank=[]
    langknown=0
    candlangtuple= ()
    for candkey in range(0,len(self.uniqueCand)):
        for langkey in range(len(self.uniqueCand), self.matrixlength):
            if(self.edges[candkey][langkey]==1):
                langknown += 1
            candlangtuple = (candkey, langknown)
        print(candlangtuple)
        langknown=0
        interpreterRank.append(candlangtuple)
    
    
    return(interpreterRank)
    
    

def maxInterpreterRank(self, ir):

    temp = 0
    interpreterRank=ir
    temprank = ()
    if len(interpreterRank) > 1:
        for rank in interpreterRank:
            if rank[1] > temp:
                temprank = rank
                i=-1
        for i in range(len(interpreterRank)):
            if i == temprank[0]:
                interpreterRank = interpreterRank[0:i] + interpreterRank[i+1:]
    else:
        temprank = interpreterRank[0]
    
    return(temprank, interpreterRank)


'''
def findMaxLanguageCand(self):
    candcount = len(self.uniqueCandidates)
    candlanguage=[]
    for i in range(candcount):
        for j in range(self.matrixlegth):
            if (self.edges[i][j]== 1 ):
                langcount+ = 1
def abc():
    for i in range(len(self.uniqueCandidates)):
        for j in range(len(self.matrixlength)self.edges[i][j]):
'''