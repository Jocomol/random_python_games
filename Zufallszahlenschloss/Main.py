'''
Created on 14.12.2016

@author: bmeiej
'''
#_#IMPORTS#_#
import RPi.GPIO as GPIO
import time
from code import Code
#!/usr/bin/python
# -*- coding: utf-8 -*-

#_#INITSALISIERUNG UND DEFINITIONEN#_#
running = True
codekorrekt= False
versuche = 8
Code = Code()
GPIO.cleanup()
GPIO.warnings(False)
GPIO.setmode(GPIO.BOARD) 
GPIO.setup(24, GPIO.OUT)#   LED 1
GPIO.setup(22, GPIO.OUT)#   LED 2
GPIO.setup(12, GPIO.OUT)#   LED 3
GPIO.setup(8, GPIO.OUT)#    LED 4
GPIO.setup(26, GPIO.IN)#    Switch 1
GPIO.setup(18, GPIO.IN)#    Switch 2
GPIO.setup(16, GPIO.IN)#    Switch 3
GPIO.setup(10, GPIO.IN)#    Switch 4

#_#MAIN PROGRAMM#_#
if running == True: ##Während das true ist ist das Programm am Laufen
    username = input("Guten Tag Willkommen zum Zufallszahlenschloss bitte geben sie ihren Namen ein: ")
    if len(username) > 45:
        print ("Bitte nicht mehr als 45 Zeichen eingeben")
        usernamekorrekt = False
        while usernamekorrekt != True: ##Solange dies nicht true ist muss der Benutzer einen Benutzernamen eingeben der den Anforderungen entspricht
            username = input("Bitte geben sie ihren Namen erneut ein: ")
            if len(username) <= 45:
                usernamekorrekt = True
            else:
                print ("Bitte nicht mehr als 45 Zeichen eingeben")
                        
    print ("Bitte Warten...")
    time.sleep(2)
    print ("Eingeloggt als Benutzer: ", username)
    time.sleep(2)
    
    while codekorrekt != True or versuche != 0:
        #_#OUTPUT#_#
        print ("Bitte schauen sie jetzt zu ihrem Eingabegerät und lesen sie den Output ab")
        code = Code.code
        time.sleep(2)
        x = 0 ##Position in der Liste
        for nummer in Code.codealsliste: ##Pro nummer in der Liste
            for i in range(nummer): ##so viel wie die die nummer aus dem vorherigen gross ist
                if x == 0:
                    GPIO.output(12, True)
                    time.sleep(1)
                    GPIO.output(12, False)
                    time.sleep(1)
                elif x == 1:
                    GPIO.output(22, True)
                    time.sleep(1)
                    GPIO.output(22, False)
                    time.sleep(1)
                elif x == 2:
                    GPIO.output(24, True)
                    time.sleep(1)
                    GPIO.output(24, False)
                    time.sleep(1)
            x = x + 1 ##nächste Position
                
        #_#INPUT#_#
        print ("Bitte geben sie jetzt den Code ein")
        codefertig = False
        inputcode = -121
        while codefertig != True:
            while GPIO.input(10):
                if GPIO.input(18) != True:
                    inputcode = inputcode + 100
##                    print("Taste 2")
##                    print (inputcode)
                    time.sleep(0.3)
                elif GPIO.input(26) != True:
##                    print ("Taste 1")
                    inputcode = inputcode + 10
##                    print (inputcode)
                    time.sleep(0.3)
                elif GPIO.input(16) != True:
##                    print ("Taste 3")
                    inputcode = inputcode + 1
##                    print (inputcode)
                    time.sleep(0.3)
            codefertig = True
##            print (versuche)

        if inputcode == code:
            print(Code.code, Code.codealsliste)
            codekorrekt = True
            running = False ##Ende des Programms
            print ("Grattulation",username,"Du hast den Code richtig eingegeben")
            logon = open("Logon.txt", "w")
            logon.write("|" + username + "|" + str(Code.code) + "|" + "|" + str(versuche) + "|") ##Speichert den Username den Code und die Anzahl Verbleibende Versuche in das logon.txt file
            logon.close()
            
        elif inputcode >= code:
            print("Der Code ist zu Hoch") 
            versuche = versuche - 1
            inputcode = -121
            print(versuche,"übrig")
        else:
            print("Der Code nicht korrekt") 
            versuche = versuche - 1
            inputcode = -121
            print(versuche,"übrig")
            
    if versuche == 0:
        print("Alle Versuche aufgebraucht, der Zwischenfall wird gemeldet")
        logon = open("Logon.txt", "w")
        logon.write("|" + username + "|" + str(Code.code) + "|" + "|" + str(versuche) + "|") ##Speichert den Username den Code und die Anzahl Verbleibende Versuche in das logon.txt file
        logon.close()
     
     
     
     
     

#_#LEGENDE#_#
    ##Kommentar
    #Nicht gebrauchter Code
    #_#TITEL#_#    
    
