
class Fahrzeug:
    def __init__(self, marke, modell, baujahr, mietpreisProTag):
        self.marke = marke
        self.modell = modell
        self.baujahr = baujahr
        self.mietpreisProTag = mietpreisProTag
    
    def berechneMietkosten(self, tage):
        return self.mietpreisProTag * tage

class Auto(Fahrzeug):
    def __init__(self, marke, modell, baijahr, mietpreisProTag, sitzplaetze, kraftstofftyp):
        super().__init__(marke, modell, baijahr, mietpreisProTag)
        self.sitzplaetze = sitzplaetze
        self.kraftstofftyp = kraftstofftyp
    
    def toString(self):
        print(f'Marke: {self.marke}; Modell: {self.modell}; Baujahr: {self.baujahr}; Mietpreis pro Tag: {self.mietpreisProTag}; Sitzplätze: {self.sitzplaetze}; Kraftstofftyp: {self.kraftstofftyp}')
        
    
class Elektroauto(Fahrzeug):
    def __init__(self, marke, modell, baujahr, mietpreisProTag, akkukapazitaet, ladestand):
        super().__init__(marke, modell, baujahr, mietpreisProTag)
        self.akkukapazitaet = akkukapazitaet
        self.ladestand = ladestand
    
    def ladeBatterie(self, ladung):
        self.ladestand += ladung
        if self.ladestand > 100:
            self.ladestand = 100
    
    def toString(self):
        print(f'Marke: {self.marke}; Modell: {self.modell}; Baujahr: {self.baujahr}; Mietpreis pro Tag: {self.mietpreisProTag}; Batteriekapazität: {self.akkukapazitaet}; Ladestand: {self.ladestand}')
    

class Main:
    def __init__(self):
        self.autos = []
    
    def addAuto(self, auto):
        self.autos.append(auto)
    
    def ausgeben(self):
        for element in self.autos:
            element.toString()

main = Main()
auto1 = Auto('Audi', 'A3', 2015, 50, 5, 'Diesel')
auto2 = Auto('BMW', 'X5', 2018, 100, 7, 'Benzin')
auto3 = Elektroauto('Tesla', 'Model S', 2020, 150, 100, 50)
auto4 = Elektroauto('VW', 'ID.3', 2021, 200, 80, 30)

main.addAuto(auto1)
main.addAuto(auto2)
main.addAuto(auto3)
main.addAuto(auto4)

main.ausgeben()

auto3.ladeBatterie(30)
print(auto2.berechneMietkosten(5))