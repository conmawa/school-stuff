class Auto:
    def __init__(self, tankfuellung = 100):
        self.tankfuellung = tankfuellung # Starttankfüllung
        
    def fahren(self):
        print ("Das Auto fährt.")
        self.tankfuellung -= 10 #Verbrauche etwas Bezin
        self.benzinMelden() # Überprüfung für Ereignisse
        
    def benzinMelden(self):
        if self.tankfuellung <= 20: # Ereignis
            print(f"Warnung: Niedriger Tankfüllstand! Nur noch {self.tankfuellung}% im Tank.")
            
class Fahrer:
    def __init__(self, auto):
        self.auto = auto
        
    def fahreAuto(self):
        self.auto.fahren() #Botschaft an das Auto-Objekt
        
meinAuto = Auto()
fahrer = Fahrer(meinAuto)

for _ in range(10):
    fahrer.fahreAuto()