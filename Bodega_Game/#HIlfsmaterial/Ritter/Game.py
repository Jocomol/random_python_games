'''
Created on 17.11.2015

@author: npeisy
'''
from burg.Ritter import Ritter
from hoele.Drachen import Drachen
from random import Random

artur = Ritter("Artur", 4, 2) # Name, Stärke, Rüstung
wilhelm = Ritter("Wilhelm", 5, 1) # Name, Stärke, Rüstung
hansPeter = Drachen("Hans Peter", 7) # Name, Stärke
dorothea = Drachen("Dorothea", 7) # Name, Stärke

kreaturenListe = [artur, wilhelm, hansPeter, dorothea]

zufall = Random()
zufallKreaturenIndex1 = -1
zufallKreaturenIndex2 = -1

while (len(kreaturenListe) > 1):
    zufallKreaturenIndex1 = zufall.randint(0, len(kreaturenListe) - 1)
    zufallKreaturenIndex2 = zufall.randint(0, len(kreaturenListe) - 1)
    while zufallKreaturenIndex1 == zufallKreaturenIndex2:
        zufallKreaturenIndex2 = zufall.randint(0, len(kreaturenListe) - 1)
    if isinstance(kreaturenListe[zufallKreaturenIndex1], Drachen):
        kreaturenListe[zufallKreaturenIndex1].fliegen(zufall.getrandbits(1))
    if isinstance(kreaturenListe[zufallKreaturenIndex2], Drachen):
        kreaturenListe[zufallKreaturenIndex2].fliegen(zufall.getrandbits(1))
        
    kreaturenListe[zufallKreaturenIndex1].angreifen(kreaturenListe[zufallKreaturenIndex2])
    if kreaturenListe[zufallKreaturenIndex2].istAmLeben() == False:
        kreaturenListe.remove(kreaturenListe[zufallKreaturenIndex2])
    
    

print("\nGewonnen hat: " + str(kreaturenListe[0].name) + "\n")
kreaturenListe[0].anzeigen()
