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
   
'''
def findMaxLanguageCand(self):
    candcount = len(self.uniqueCandidates)
    candlanguage=[]
    for i in range(candcount):
        for j in range(self.matrixlegth):
            if (self.edges[i][j]== 1 ):
                langcount+ = 1
'''                