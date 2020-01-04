# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 08:46:41 2019

@author: SaurabhX360
"""

  
class interPretr:
    #import readApplications
    def __init__(self):
        self.parseline=[] #parsing the inout lines into words - candidate and languages
        self.uniqueCand=[]
        self.uniqueLang=[]
        self.vertices=[] #list containing interpreter and languages
        self.edges=[[],[]] #adjacency matrix of edges linking interpreters to languages
        self.infile = ''
        self.matrixlength=0
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
        
        self.vertices = self.uniqueCandidates() + self.uniqueLanguages()
        print('________ Initial Adjacency Matrix_________')
        self.edgeinit()
        self.displayedges()
        self.edgebuilder()
        self.displayedges()
        #
        #print(self.vertices, len(self.vertices))
        
        
    def edgeinit(self):
        self.matrixlength=len(self.vertices)
        self.edges=[[None for i in range(self.matrixlength)] for j in range(self.matrixlength)]
        
        for i in range(self.matrixlength):
            for j in range(self.matrixlength):
                self.edges[i][j]='.'
        
    
    def displayedges(self):    
        for word in self.vertices:
            print(word[0],'', end='')
        print('\n')
        for i in range(self.matrixlength):
            for j in range(self.matrixlength):
                endchar='_'
                if (j+1)//self.matrixlength==0:
                    endchar = ' '
                else:
                    endchar = '\n'
                print(self.edges[i][j],end=endchar)
                
        print('_______ Dimensions of matrix - ', self.matrixlength, '^2_____  ')
        
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

    def displayCandidates(self, lang):
        print("--------Function Display Candidates --------")
        print('\n')
        print("SearchLanguage: ", lang)
        
        
        langKey = self.findLanguageKey(lang) 
        translators = []
        if (langKey==-1):
            print("No candidate knows %s language." %lang)
        else:
            for i in range(len(self.vertices)):
                if (self.edges[i][langKey]==1):
                    translators.append(self.vertices[i])
            print('List of candidates who can speak %s:\n%s ' %(lang, ('\n').join(translators)) )
            
        
    def findDirectTranslator(self, langA, langB):

        print("--------Function findDirectTranslator --------")
        print('\n')
        print("Language A: ", langA)
        print("Language B: ", langB)
        
        langAKey=self.findLanguageKey(langA)
        langBKey=self.findLanguageKey(langB)
        
        if (langAKey == -1 or langBKey == -1):
            print("This language does not exist with any candidate, please select different languages. ")
            return 0
        else:
            translatorfound = False
            
            translators = []
            count=0
            
            for i in range(len(self.vertices)):
                if (self.edges[i][langAKey] == 1 and self.edges[i][langBKey] == 1):
                    print("Yes, %s can translate. " % self.vertices[i])
                    translatorfound = True
                    count+=1
                    translators.append(self.vertices[i])
            
            count= 0
            if translatorfound is False:
                print("Direct Translator: No" )
                print('\n')
                return 0
            else:
                print("Total %d translator(s) can translate from %s to %s, and they are: %s." %(count, langA, langB, ', '.join(translators)) )
                print('\n')
                return 1    


    def findTransRelation(self, langA, langB):
        
        ''' First   - check for direct translator'''
        ''' Second  - check for TransRelation'''
        ''' @@@@@@@@@@@@@@@ Display will be repaeated for direct translator '''
        
        print("--------Function findTransRelation --------")
        print("\n")
        print("Language A: ", langA)
        print("Language B: ", langB)
        
        transrelation=False
        if(self.findDirectTranslator(langA, langB)==0):
            langC="Yet-to-be-coded"
            cand1="tbd-cand1"
            cand2="tbd-cand2"
            transrelation = True
            if transrelation:
                print("Related: Yes, %s > %s > %s > %s > %s" %(langA, cand1, langC, cand2, langB) )
            else:
                print("There are no direct or transitive relation translators available for languages %s and %s.", (langA, langB) )
        else:
            print("As there are direct translators available there is no need for transitive relation translators")
        
    
            
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

    def showAll(self):
        self.uniqueCand = self.uniqueCandidates()
        self.uniqueLang = self.uniqueLanguages()
        
        print('Total no. of candidates: ', len(self.uniqueCand))
        print('Total no. of languages: ', len(self.uniqueLang))
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