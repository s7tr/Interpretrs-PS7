# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 16:11:19 2020

@author: SaurabhX360
"""

from interPretr import interPretr

ip=interPretr()
ip.readApplications('inputfile.txt')

#ip.testparseline()
#ip.showAll()
ip.findDirectTranslator('English', 'Hindi')
ip.findDirectTranslator('Armenian', 'French')
ip.findDirectTranslator('English', 'German')
ip.findDirectTranslator('Tamil', 'Hindi')
ip.findDirectTranslator('English', 'German')
ip.findTransRelation('English', 'Russian')
ip.displayCandidates('English')
ip.displayCandidates('Tamil')
ip.displayCandidates('Bingo')

#ip.createvertices()
#ip.createedges()
#ip.uniqueCand, countcand = ip.uniqueCandidates()
#ip.uniqueLang, countlang = ip.uniqueLanguages()
#ip.createvertices()
