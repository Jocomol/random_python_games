'''
Coded by Joel 'Jocomol' Meier
Contact me at: joelmeier08@gmail.com
'''

##imports


##classes
class Player:

    ##attributes
    name = ""
    homeplanet = ""
    strenght = 1
    health = 1
    speed = 1
    shield = 1
    charisma = 1
    weapon = "Civilian Blaster"
    blaster_damage = 1
    bolts = 12
    magazin_size = 6


    ##functions
    def __init__(self, name, planet, strenght, health, speed, shield, charisma):
        self.name = name
        self.homeplanet = planet
        self.strenght = strenght
        self.health = health
        self.speed = speed
        self.shield = shield
        self.charisma = charisma

    def inventory(self):
        return "Name: " + self.name + " from " + self.homeplanet + "\n" \
            "strenght: " + str(self.strenght) + "\n" \
            "health: " + str(self.health) + "\n" \
            "speed: " + str(self.speed) + "\n" \
            "shield: " + str(self.shield) + "\n" \
            "charisma: " + str(self.charisma) + "\n" \
            "Weapon: " + (self.weapon) + "\n"

    def attack(self, enemy):
        playerdamage = self.shoot()
        enemy.take_damage(playerdamage)


    def shoot(self):
        if self.bolts == 0:
            print("\n\"CLICK\" Your Weapon has no Bolts left")
        else:
            self.bolts = self.bolts - 1
            damage = int(self.blaster_damage)
            return damage
            print ("PZZZZW")

    def isAlive(self):
        if self.health <= 0:
            return False
        else:
            return True

    def take_damage
    
