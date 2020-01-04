# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 08:46:41 2019

@author: SaurabhX360
"""

#import showAll    
class interPretr:
    #import readApplications
    def __init__(self):
        self.parseline=[] #parsing the inout lines into words - candidate and languages
        self.uniqueCand=[]
        self.uniqueLang=[]
        self.vertices=[] #list containing interpreter and languages
        self.edges=[[]] #adjacency matrix of edges linking interpreters to languages
        self.infile = ''
        #def readApplications
        # sample infile content 
        # No of candidates required to cover all languages: 5
        # Manasa / English / Hindi / Punjabi
        # Venkat / English / Kannada / Tamil / Telugu
        # Paul / Malayalam / Marathi / Tamil / Telugu
        # Harish / Punjabi / Gujarati / English / Hindi
        # Nisha / Bengali / English / Marathi / Hindi    
    
    def readApplications(self, infile):
    
        f=open(infile,"r")
        for rawline in f:
            #print(rawline)
            rawline = rawline.strip()
            
            candidate = []
            word=''
            l=len(rawline)
            
            for i, c in enumerate(rawline):        
                if c == ' ':
                    pass
                elif c == '/':
                    candidate.append(word)
                    word=''
                else:
                    word+=c
                if i == l-1:
                    candidate.append(word)
                    word=''
                #print(i, l, word, candidate)
            
            self.parseline.append(candidate)

        f.close()
                    
    def uniqueCandidates(self):
        self.uniqueCand=[]
        countcand=0
        for pline in self.parseline:
            plinecand = pline[0]
            if plinecand not in uniqueCand:
                self.uniqueCand.append(plinecand)
                countcand+=1
        return self.uniqueCand, countcand
    
    def uniqueLanguages(self):
        self.uniqueLang=[]
        countlang=0
        for pline in self.parseline:
            plinelang = pline[1:]
            for lang in plinelang:
                if lang not in uniquelang:
                    self.uniqueLang.append(lang)
                    countlang+=1
        return self.uniqueLang, countlang
    
    def createvertices(self):
        for cand in self.uniqueCand:
            self.vertices.append(cand)
        for lang in self.uniqueLang:
            self.vertices.append(lang)
        print(self.vertices)

    def showAll(self):
        self.uniqueCand, countcand = ip.uniqueCandidates()
        self.uniqueLang, countlang = ip.uniqueLanguages()
        
        print('Total no. of candidates: ', countcand)
        print('Total no. of languages: ', countlang)
        print('\n')
        print('List of candidates: ')
        for cand in self.uniqueCand:
            print(cand)
        print('\n')
        
        print('List of languages: ')
        for lang in self.uniqueLang:
            print(lang)
        
    def testparseline(self):
        print(self.parseline)
        print('------------------parseline-------------------------------')
        for pline in self.parseline:
            print(pline)
        print('---------------------------------------------------------')

    def createedge(self):
        dictcand={}
        i = 0
        for cand in self.uniqueCand:
            dictcand[cand] = i
            i+=1
        print(dictcand)
            
        dictlang={}
        i = 0
        for lang in uniqueLang:
            dictlang[lang] = i
            i+=1
        print(dictlang)
        

        w=len(self.uniqueLang)
        h=len(self.uniqueCand)
        #self.edges = [[0]*h]*w
        self.edges = [ [ 0 for i in range(w) ] for j in range(h) ]
        print(self.edges)
        adjlist = [0 for i in range(w)]
        print(adjlist)
        for i, vertex in enumerate(self.vertices):
            for j, lang in enumerate(vertex[1:]):
                k = dictlang.get(lang,99)
                adjlist[k]=1
                self.edges[i][0]=adjlist
                #self.edges[[i][k]] = 1
                #self.edges[[i],[j]] = dictlang.get(lang)
                #self.edges[[i][j]] = dictlang.get(lang)
                #self.edges[i][j] = 
        print(self.edges)     
'''        
        for i, pline in self.parseline:
            for j, x in enumerate(pline):
                if self.edges[i][j] = dictcand[pline[0]]
         '''        

ip=interPretr()
ip.readApplications('inputfile.txt')
ip.testparseline()
ip.showAll()

ip.uniqueCand, countcand = ip.uniqueCandidates()
ip.uniqueLang, countlang = ip.uniqueLanguages()
ip.createvertices()
 
'''        
       0 1 2 3 4 5 6 7 8 9 
     0 . .   . . .   . .
     1   . . .    .      .  
     2   .      .      .
     3             . .
     4   . . .     . . . .

'''     

    

#ip.edgecreator()

#candidates,candcount = ip.uniqueCandidates()
#languages,langcount = ip.uniqueLanguages()
#print('----------------------unique candidates------------------')
#print(candidates,candcount)
#print('---------------------------------------------------------')
#print('----------------------unique languages-------------------')
#print(languages,langcount)
#print('---------------------------------------------------------')