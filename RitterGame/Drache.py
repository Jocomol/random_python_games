'''
Created on 23.11.2016

@author: Jocomol
'''
from random import *
class Drache:
    
    name = ""
    staerke = 0
    leben = 20
    
    def __init__(self, name, staerke):
        self.name = name
        self.staerke = staerke
            
    
    def anzeigen(self):
        return "Name: " + self.name + "\n" \
            "Stärke: " + str(self.staerke) + "\n" \
            "Leben: " + str(self.leben) + "\n"
        return result
        
    def verteidigen(self, staerkeGegner):
        self.leben = self.leben - staerkeGegner
        print(self.name + " wird angegriffen mit Stärke " 
              + str(staerkeGegner) + ". Leben neu: " 
              + str(self.leben))
        
    def angreifen(self, gegner):
        print (self.name + " greift an")
        gegner.verteidigen(self.staerke)
        
    def feuerspucken(self, gegner):
        print (self.name,"spuckt Feuer")
        self.staerke = self.staerke + 5
        gegner.verteidigen(self.staerke)
        self.staerke = self.staerke - 5
    
    def istAmLeben(self):
        if self.leben <= 0:
            return False
        else:
            return True
    
    def attacke(self,gegner):
        act = randint(1,100)
        if act >= 1 and act < 50:
            self.angreifen(gegner)
        elif act > 50 and act <= 80:
            print(self.name,"hat verfehlt")
        else:
            self.feuerspucken(gegner)

    