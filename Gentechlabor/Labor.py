from Pflanse import Pflanze
from random import randint
import time
startend = False
rdy = False

farben = ["grün", "gelb", "schwarz", "rot"]


while startend != True:
    print ("Hallo das hier ist der Umlitamo Blumenmacher")
    action = input("Willst du 10 Zufällige oder 1 Benutzerdefinierte Pflanzen erstellen? <b> oder <z>")



    if action == "b":
        startend = True
        while rdy != True:
            pn = input("Wie willst du deine Pflanze Benenen? ")
            pc = input("Welche Farbe soll die Pflanze haben? ")
            ph = int(input("Wie gross soll die Pflanze sein? (in cm) "))
            pb = int(input("Wie vile Blätter soll die Pflanze Haben? "))
            
            if ph < 5 or ph > 20:
                print("Fehler die Pflanze muss zwischen 5-20 cm gross sein")
            elif pb < 4 or pb > 15:
                print ("Fehler die Pflanze muss zwischen 4-15 Blätter haben")
            else:
                ph = str(ph)
                pb = str(pb)
                ph = ph + " cm"
                
                print ("Die Pflanze wird erstellt")
                time.sleep(5)
                plant = Pflanze(pn, pc, ph, pb)
                plant.getInfos()
                rdy = True
    
    elif action == "z":
        startend = True
        for i in range(11):
            
            cn = randint(0,3)
            hn = str(randint(5,21))
            bn = str(randint(4,16))
            
            name = "Pflanze " + str(i)
            hn = hn + " cm"
            color = farben[cn]
        
            plant = Pflanze(name, color, hn, bn)
        
            plant.getInfos()
    else:
        print("Gib bitte <b> oder <z> ein")