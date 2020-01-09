# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 08:46:41 2019

@author: SaurabhX360
"""

class interPretr:

    '''
    This class file contains the mandatory functions needed as per PS7
    Any functions that are user defined, are part of the _ps7func file & are imported
    '''

    from _ps7func import edgeinit
    from _ps7func import edgebuilder
    from _ps7func import findCandidateKey
    from _ps7func import findLanguageKey
    from _ps7func import uniqueCandidates
    from _ps7func import uniqueLanguages
    from _ps7func import createvertices
    
    from _ps7func import removeCovLang
    from _ps7func import getInterpreterRank
    from _ps7func import maxInterpreterRank
    
    
    from _ps7func_testfun import testparseline
    from _ps7func_testfun import testdisplayedges

    
    def __init__(self):
        self.vertices=[] #list containing interpreter and languages
        self.edges=[[],[]] #adjacency matrix of edges linking interpreters to languages
        '''
        Additional variables to store unique lists of candates/translators and languages
        '''
        self.parseline=[]   #parsing the inout file lines into words - candidate and languages
        self.uniqueCand=[]  #Unique Candidate List
        self.uniqueLang=[]  #Unique Language List

        self.infile = ''
        self.matrixlength=0
        
        self.hireList = []
        
    def promptsReader(self):
        
        '''
        # yet to be coded
        @@@ this function reads the command prompts from the promptsPS7 TEXT file
        and invokes the relevant functions
        '''

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

        '''
        Adding the Unique candidates and languages together
        This gives the list of nodes that required in Adjacency matrix
        '''

        self.vertices = self.uniqueCandidates() + self.uniqueLanguages()

        print('________ Initial Adjacency Matrix_________')
        self.edgeinit()
        self.testdisplayedges()
        self.edgebuilder()
        self.testdisplayedges()
        #
        #print(self.vertices, len(self.vertices))


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

       
        visited = [False for i in range(len(self.vertices))]
        print(visited)

        stack = []
        stack.append(langA)
        print(stack)
    
        while(len(stack)):
            s = stack[-1]
            print(s)
            stack.pop()
    
            if(not visited[s]):
                print(s,end=' ')
                visited[s] = True
    
            for node in self.edges[s]:
                if(node == langB):
                    print(langB, end=' ')
                    return True
                if(not visited[node]):
                    stack.append(node)
    
        return False
        '''
        transrelation=False
        if(self.findDirectTranslator(langA, langB)==0):
            @@@@@@@@@@@@@ Yet to be completed @@@@@@@@@@@@@
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
        '''
        
    def displayHireList(self):
        
        tobeCovLang= self.vertices
        interpreterRank = self.getInterpreterRank()
        maxrank, interpreterRank = self.maxInterpreterRank(interpreterRank)
        
        candKey = maxrank[0]
        self.hireList.append(self.uniqueCand[candKey])
        self.removeCovLang(candKey, tobeCovLang)
        print(self.hireList)
        print(tobeCovLang)
        '''
        for l in range():
            if self.edges[candKey][l] == 1:
                self.removeCovLang(l)
        '''        
        
        print(interpreterRank)
        
