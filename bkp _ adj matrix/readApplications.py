# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 13:41:19 2019

@author: SaurabhX360
"""


    readApplications(self, infile):
        
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
            
            self.vertices.append(candidate)
    
        f.close()
        
        
    def testvertices(self):
        print('------------------Vertices-------------------------------')
        for vertex in self.vertices:
            print(vertex)
        print('---------------------------------------------------------')
    
    #def edgecreate(self):
        
    '''
    def edgecreator(self):
        candidates,candcount = ip.uniqueCandidates()
        languages,langcount = ip.uniqueLanguages()
        
        for cand in candidates:
            for lang in languages:
                    
                    adjcmatentry = (cand, lang)
                
                
            if candidate in self.vertices[[][0]]:
                print(candidate)
       '''     
        
