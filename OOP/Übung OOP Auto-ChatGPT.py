## Aufgabe von ChatGPT ##

class Auto:
    def __init__(self, marke, farbe, geschwindigkeit = 0):
        self.marke = marke
        self.farbe = farbe
        self.geschwindigkeit = geschwindigkeit
    
    def beschleunigen(self, wert):
        self.geschwindigkeit += wert
    
    def fahren(self):
        print("fahren")
        
class Elektroauto(Auto):
    def __init__(self, marke, farbe, geschwindigkeit = 0, reichweite = 0):
        super().__init__(marke, farbe, geschwindigkeit)
        self.reichweite = reichweite
        
    def ladebatterie(self):
        while self.reichweite != 300:
            self.reichweite += 10
            
        print(f"Elektroauto ist geladen. Neue Reichweite: {self.reichweite}km")
    
    def fahren(self):
        while self.reichweite > 0:
            print("fahren")
            self.reichweite -= 10
        
        print("Autobatterie ist leer! Auto kann nicht weiter fahren")
            
        
def fahren(auto):
    auto.fahren()

auto = Auto("Mercedes", "grün")
e_auto = Elektroauto("Tesla", "weiß")

print(auto.marke)
print(auto.farbe)
print(auto.geschwindigkeit)
auto.beschleunigen(100)
print(auto.geschwindigkeit)
#print(e_auto.geschwindigkeit)
e_auto.ladebatterie()

fahren(e_auto)


