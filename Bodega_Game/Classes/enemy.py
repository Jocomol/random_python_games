'''
Coded by Joel 'Jocomol' Meier
Contact me at: joelmeier08@gmail.com
'''

##imports

##classes
class Enemy:

    ##attributes
    name = ""
    strenght = 1
    health = 1
    speed = 1
    shield = 1
    charisma = 1
    weapon = "Civilian Blaster"


    ##functions
    def __init__(self, name,strenght, health, speed, shield, charisma):
        self.name = name
        self.strenght = strenght
        self.health = health
        self.speed = speed
        self.shield = shield
        self.charisma = charisma

    def isAlive(self):
        if self.health <= 0:
            return False
        else:
            return True
