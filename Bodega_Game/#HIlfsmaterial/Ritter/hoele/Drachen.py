'''
Created on 17.11.2015

@author: npeisy
'''

class Drachen:
    name = ""
    staerke = 0
    leben = 15
    fliegt = False
    feuerStaerke = 5
    


    def __init__(self, name, staerke):
        self.name = name
        self.staerke = staerke
        
    def fliegen(self, sollFliegen):
        self.fliegt = sollFliegen
        
    def anzeigen(self):
        print("***********************************")
        print("Ritter: " + self.name)
        print("Staerke: " + str(self.staerke))
        print("Leben: " + str(self.leben))
        print("***********************************")
    
        
    def verteidigen(self, staerkeGegner):
        if self.fliegt:
            print("Der Drache %s kann nicht angegriffen werden da er fliegt." % (self.name))
        else:
            self.leben = self.leben - staerkeGegner
            print(self.name + " wird angegriffen mit Stärke " 
              + str(staerkeGegner) + ". Leben neu: " 
              + str(self.leben))
            
    def angreifen(self, gegner):
        gegner.verteidigen(self.staerke)
        
        
    def feuerSpucken(self, gegner):
        if self.fliegt:
            gegner.verteidigen(self.staerke + self.feuerStaerke)
        else:
            print("Der Drache %s kann nicht feuer spucken, da er nicht fliegt." % (self.name))
            
    def istAmLeben(self):
        return self.leben > 0