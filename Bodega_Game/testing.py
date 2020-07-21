'''
Coded by Joel 'Jocomol' Meier
Contact me at: joelmeier08@gmail.com
'''

##imports
from random import *
import time
from Classes.Player import Player
from Classes.enemy import Enemy

##Objects and Enititys
testobject = Player("Testor", "Testonia", 1, 1, 2, 3, 5) #name, homeplanet, strenght, health, speed, shield, charsima
#testenemy

##Arrays
T_17 = ["T-17",1,12,6]

##definitions
def new_weapon(weapon_array):
    new_weapon_take = False
    print ("\nYou found a",weapon_array[0],"its damage is",weapon_array[1],"and it has a Magain Size of",weapon_array[3],"\n")
    print ("Also you found", weapon_array[2], "Bolts whit it")
    while new_weapon_take == False:
        take_weapon = input("\nDo you want to [T]ake your old Weapon or [K]eep your Current Weapon the WEAPON_2 ")
        if take_weapon == "T" or take_weapon == "t":
            testobject.weapon = weapon_array[0]
            testobject.blaster_damage = weapon_array[1]
            testobject.bolts = weapon_array[2]
            testobject.magazin_size = weapon_array[3]
            new_weapon_take = True
            print ("\nYou got a",testobject.weapon,"its damage is",testobject.blaster_damage,"and it has a Magain Size of",testobject.magazin_size,"\n")
        elif take_weapon == "K" or take_weapon == "k":
            print("\nYou keep your old Weapon")
            new_weapon_take = True
        else:
            ("\nPLS write K or T not",take_weapon,"I mean you surley want to Continoue")


##Testing _Area (Keep the Code)
print ("\n" + testobject.inventory())
start_testenviroment = input("Press Enter to start the Testing Enviroment ")
new_weapon(T_17)
print ("\n" + testobject.inventory())
##Weapon pickup
#action = input("Take weapon [y]/[n]: ")
#if action == "y":
    #testobject.weapon = "Military Blaster"
#elif action == "n":
    #print ("no weapons")
#print ("\n" + testobject.inventory())

##Battle
