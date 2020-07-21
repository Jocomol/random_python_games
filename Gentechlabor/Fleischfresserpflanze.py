'''
Created on 30.11.2016

@author: Jocomol
'''
from Pflanse import Pflanze
from Moskito import Moskito

class Fleischfresserpflanze(Pflanze):
    Moskito = None
    mengeWasserZumWachsen = 1
    naeherwertZumWachsen = 3
    naehrWertKonsumiert = 0
    
    def fuettern(self, Moskito):
        self.naehrWertKonsumiert = self.naehrWertKonsumiert + Moskito.naehrwert
        self.Moskito = None
        self.Moskito = Moskito
        print(Moskito)
        
    def hatGenugFutter(self):
        if self.Moskito != None and (Moskito.naehrwert + self.naehrWertKonsumiert) >= self.naeherwertZumWachsen:
            return True
        else: 
            return False
    
    def wachsen(self):
        if self.wasser >= self.mengeWasserZumWachsen and Moskito != None and Moskito.naehrwert >= self.naeherwertZumWachsen:
            self.groesse = self.groesse + 1
            Moskito.naehrwert = Moskito.naehrwert - self.naeherwertZumWachsen  
            print ("Deine Pflanze ist gewachsen")   
        else:
            print("Deine Pflanze kann noch nicht Wachsen")
            print(Moskito.naehrwert, self.wasser, self.naehrWertKonsumiert)
    