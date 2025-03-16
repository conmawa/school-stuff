class Fahrrad:
    def __init__(self, modell, marke, preis, mietgebuehr):
        self.modell = modell
        self.marke = marke
        self.preis = preis
        self.mietgebuehr = mietgebuehr
        self.verfuegbar = True
    
    def fahrraf_info(self):
        return f"Modell: {self.modell}, Marke: {self.marke}, Preis: {self.preos}, Mietgebuehr: {self.mietgebuehr}, Verfuegbarkeit: {self.verfuegbar}"
    
    def berechne_mietkosten(self, tage):
        return self.mietgebuehr * tage