## Vererbung ##

class Fahrzeug():
    def __init__(self, marke):
        self.marke = marke
        
    def fahren(self):
        return "Dieses Fahrzeug fährt!"
    

class Auto(Fahrzeug):
    def __init__(self, marke, modell):
        super().__init__(marke)
        self.modell = modell
    
    def hupen(self):
        return "Das Auto hupt"
    
mein_auto = Auto("Mercedes-Benz", "G-Klasse")
print(mein_auto.fahren())
print(mein_auto.hupen())