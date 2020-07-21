'''
Created on 17.11.2015

@author: npeisy
'''

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
        print("***********************************")
        print("Ritter: " + self.name)
        print("Staerke: " + str(self.staerke))
        print("Ruestungswert: " + str(self.ruestung))
        print("Leben: " + str(self.leben))
        print("***********************************")
        
    def verteidigen(self, staerkeGegner):
        self.leben = self.leben - (staerkeGegner - self.ruestung)
        print(self.name + " wird angegriffen mit Stärke " 
              + str(staerkeGegner) + ". Leben neu: " 
              + str(self.leben))
        
    def angreifen(self, gegner):
        gegner.verteidigen(self.staerke)
    
    def istAmLeben(self):
        return self.leben > 0
        