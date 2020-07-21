'''
Created on 17.11.2015
Modified on 23.11.2016

@author: npeisy
@modifier: Jocomol
'''
from random import *
class Ritter:
    
    name = ""
    staerke = 0
    ruestung = 0
    leben = 20
    
    def __init__(self, name, staerke, ruestung):
        self.name = name
        self.staerke = staerke
        self.ruestung = ruestung      
    
    def anzeigen(self):
        return "Name: " + self.name + "\n" \
            "Stärke: " + str(self.staerke) + "\n" \
            "Rüstung: " + str(self.ruestung) + "\n" \
            "Leben: " + str(self.leben) + "\n"
        return result
        
    def verteidigen(self, staerkeGegner):
        self.leben = self.leben - (staerkeGegner - self.ruestung)
        print(self.name + " wird angegriffen mit Stärke " 
              + str(staerkeGegner) + ". Leben neu: " 
              + str(self.leben))
        
    def bogen(self, gegner):
        self.staerke = self.staerke - 1
        print (self.name + " Benutzt einen Bogen")
        gegner.verteidigen(self.staerke)
        self.staerke = self.staerke + 1
    
    def schlag(self, gegner):
        print (self.name + " greift an")
        gegner.verteidigen(self.staerke)
        
    def istAmLeben(self):
        if self.leben <= 0:
            return False
        else:
            return True 
          
    def attacke(self,gegner):
        act = randint(1,100)
        if act >= 1 and act < 50:
            self.schlag(gegner)
        elif act > 50 and act <= 60:
            print(self.name,"hat verfehlt")
        else:
            self.bogen(gegner)
    
        
