# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 00:30:50 2020

@author: SaurabhX360
"""

def testparseline(self):
    print(self.parseline)
    print('------------------parseline-------------------------------')
    for pline in self.parseline:
        print(pline)
    print('---------------------------------------------------------')

def testdisplayedges(self):    
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