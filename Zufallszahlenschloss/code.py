'''
Created on 14.12.2016

@author: bmeiej
'''
#_#IMPORTS#_#
import time
from random import randint
#!/usr/bin/python
# -*- coding: utf-8 -*-

class Code:
    
    #_#INITS UND DEFS#_#
    code = 0
    codeasliste = [0,0,0]
    
    def __init__(self): ##Der Initalisierer
        self.codealsliste = self.codelistengenerator()
        self.code = self.listezucode(self.codealsliste)

    def codelistengenerator(self):
        listcodegen = [0,0,0]
        for i in range(3):
            coderndm = randint(3,5)
            listcodegen[i] = coderndm
        return listcodegen

    
    def listezucode(self, liste): ##Erstellt aus der Liste einen code als Integer(wichtig fuer die ueberpruefung des input)
        codeteil1 = (liste[0]) * 100
        codeteil2 = (liste[1]) * 10
        codeteil3 = liste[2]
        code = codeteil1 + codeteil2 + codeteil3
        return code
