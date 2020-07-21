'''
Created on 30.11.2016

@author: Jocomol
'''

from Pflanse import Pflanze

class Rose(Pflanze):
    mengeWasserZumWachsen = 3
    
    def __init__(self, name, farbe, groesse, anzahlblatt):
        Pflanze.__init__(self, name, farbe, groesse, anzahlblatt)
        