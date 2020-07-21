class Pflanze:
    name = ""
    farbe = ""
    groesse = 0
    anzahlblatt = ""
    wasser = 0
    mengeWasserZumWachsen = 0
    
    def __init__(self, name, farbe, groesse, anzahlblatt):
        self.name = name
        self.farbe = farbe
        self.groesse = groesse
        self.anzahlblatt = anzahlblatt
        
    def hatGenugWasser(self):
        if self.wasser >= self.mengeWasserZumWachsen:
            return True
        else:
            return False
        
    def wasserGeben(self, menge):
        self.wasser = self.wasser + menge
        
    def wachsen(self):
        possible = self.hatGenugWasser()
        if possible == True:
            self.wasser = self.wasser - self.mengeWasserZumWachsen
            self.groesse = self.groesse + 1
            print("Deine Pflanze ist Gewachsen")
            self.getInfos()
        else:
            print ("Deine Pflanze hat nicht genug Wasser zum Wachsen")
        
    
    def getInfos(self):
        water = str(self.wasser)
        print ("Name:",self.name)
        print ("Farbe:",self.farbe)
        print ("Grösse:",self.groesse)
        print ("Anzahl der Blütenblätter:",self.anzahlblatt)
        print ("Die Pflanze hat " + water + " Wasser")
        print ("")