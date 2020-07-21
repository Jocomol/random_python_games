'''
Created on 17.11.2015
Modified on 23.11.2016

@author: npeisy
@modifier: Jocomol
'''
from Ritter import Ritter
from Drache import Drache
from random import *
import time 

endfight = False
rdy = False

artur = Ritter("Artur", 4, 3) ##(Name, Stärke, Rüstung)
wilhelm = Ritter("Wilhelm", 5, 1)
#werner= Ritter("Werner", 2, 5)
zurion = Drache("Zurion", 6) ##(Name, Stärke)
shiniqua = Drache("Shiniqua", 5)
#gandalf = Magier("Gandalf",attacke, mana) ##(Name, Stärke, Mana)
#dumbledore = Magier("Dumbledore",attacke, mana)

gladiator = [artur, wilhelm, zurion, shiniqua]

while rdy != True:
    attacker = gladiator[randint(0,3)]
    defender = gladiator[randint(0,3)]
    #attacker = werner ##Testing purposes
    #defender = artur
    if attacker == defender:
        quit
    else: 
        rdy = True
        print ("Es kämpft " + attacker.name + " gegen " + defender.name)
        time.sleep(1)
        print ("Ready")
        time.sleep(1)
        print ("KEINE GNADE")
        print ("")
        print ("")

while attacker.istAmLeben() == True and defender.istAmLeben() == True:
    
    time.sleep(2)
    attacker.attacke(defender)
    print ("")
    
    if attacker.istAmLeben() == False or defender.istAmLeben() == False:
        break
    
    time.sleep(2)
    defender.attacke(attacker)
    print ("")
    
    if attacker.istAmLeben() == False or defender.istAmLeben() == False:
        break
    
if attacker.istAmLeben() == True: 
    gewinner = attacker
else:
    gewinner = defender

print("\nGewonnen hat: \n")
print(gewinner.anzeigen())
