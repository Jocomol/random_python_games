'''
Coded by Joel 'Jocomol' Meier
Contact me at: joelmeier08@gmail.com
'''

##imports
from random import *
import time
from Classes.Player import Player

##variables
gamerunning = True
planetchoose = False
skills = False
skillpoints = 5

##Objects and Enititys


##Arrays


##definitons
def fight():
    theplayer = player
    theenemy = current_room.enemy
    while theplayer.isAlive() == True and theenemy.isAlive == True:

    time.sleep(2)
    theplayer.attack(theenemy)
    print ("")

    if theplayer.isAlive() == False or theenemy.isAlive() == False:
        break

    time.sleep(2)
    theene,y.attack(theplayer)
    print ("")

    if theplayer.isAlive() == False or theenemy.isAlive() == False:
        break

if theplayer.isAlive() == True:
    winner = theplayer
else:
    winner = theenemy



##start
print ("Welcome to the Bodega Fangame\n")
time.sleep(2)
print ("This is a textbased game running on Python\n")
time.sleep(2)
print ("The Bodega Fangame is based on the sci-fi story of <INSERT NAME HERE>\n")
time.sleep(2)
print ("This game is in Alpha 1.0 so expect bugs and missing Features\n")
time.sleep(2)
playername = input("Please enter your name so we can finally begin: ")
time.sleep(2)
print ("\nEvery Hero, every Villain even every living thing, comes from a Planet (except the Space Whales from the Andromeda Nebula). So what is your Home Planet?")
time.sleep(4)
while planetchoose == False:
    playerplanet = input("\nThere are the Planets of Earth, Quadvar 5 and Spurloopia\nPlease choose one of them: ")
    if playerplanet == "Earth" or playerplanet == "Quadvar 5" or playerplanet == "Spurloopia":
        print ("\nSo you are",playername,"from",playerplanet + "?\nNice to meet you :)")
        planetchoose = True
    else:
        time.sleep(1)
        print ("\nWHAT THE FLARV?! I said choose one of the 3 planets and not some fictional planet! Maybe you just wrote the planet wrong...")
time.sleep(2)
print ("\nLets get to the Skillpoints, you have 5 of them Spend them wisely")
time.sleep(2)
print ("\nYou can spend them in these 5 Skills: Strenght, Health, Speed, Shield, Charisma")
time.sleep(2)
print("\nI give you time to think, just press a <ENTER> when you are Ready")
endwait = input()
time.sleep(2)
while skills == False:
    strenght = int(input("\nHow many points do you want to Spend on Strenght (Just enter the Number): "))
    skillpoints = skillpoints - strenght
    time.sleep(2)
    health = int(input("\nHow many points do you want to Spend on Health (Just enter the Number): "))
    skillpoints = skillpoints - health
    time.sleep(2)
    speed = int(input("\nHow many points do you want to Spend on Speed (Just enter the Number): "))
    skillpoints = skillpoints - speed
    time.sleep(2)
    shield = int(input("\nHow many points do you want to Spend on your Shields (Just enter the Number): "))
    skillpoints = skillpoints - shield
    time.sleep(2)
    charisma = int(input("\nHow many points do you want to Spend on your Charisma (Just enter the Number): "))
    skillpoints = skillpoints - charisma
    if skillpoints >= 0:
        print ("\nOk good...\nnow after adding the Base Skillpoints every creature has...")
        strenght =  strenght + 1
        health = health + 2
        speed = speed + 1
        shield = shield + 1
        charisma =  charisma + 1
        skills = True
    else:
        print ("\nYou used more Skillpoints than you had, You have to do the Skillpoints again")
        strenght = 1
        health = 1
        speed = 1
        shield = 1
        charisma = 1
        skillpoints = 5
player = Player(playername, playerplanet, strenght, health, speed, shield, charisma)
print ("\n" + player.inventory())
end = input()
