# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 16:11:19 2020

@author: SaurabhX360
"""
'''import interPretr class'''
#import sys
from interPretr import interPretr


'''invoke interPretr class''' 
ip=interPretr()

'''Function 1 - readApplications'''
ip.readApplications('inputfile.txt')

'''Function 2 - showAll'''
ip.showAll()

'''Function 3 - displayHireList'''

'''Function 4 - findDirectTranslator'''
ip.findDirectTranslator('English', 'Hindi')
ip.findDirectTranslator('Armenian', 'French')
ip.findDirectTranslator('English', 'German')
ip.findDirectTranslator('Tamil', 'Hindi')
ip.findDirectTranslator('English', 'German')

'''Function 5 - findTransRelation'''
ip.findTransRelation('English', 'Russian')

'''Function 6 - displayCandidates'''
ip.displayCandidates('English')
ip.displayCandidates('Tamil')
ip.displayCandidates('Bingo')

ip.displayHireList()


#ip.createvertices()
#ip.createedges()
#ip.uniqueCand, countcand = ip.uniqueCandidates()
#ip.uniqueLang, countlang = ip.uniqueLanguages()
#ip.createvertices()