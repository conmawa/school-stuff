from fahrrad import *

class Mountainbike(Fahrrad):
    def __init__(self, modell, marke, preis, federung):
        super().__init__(modell, marke, preis, 30)
        self.federung = federung
