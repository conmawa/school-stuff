from fahrrad import *

class Citybike(Fahrrad):
    def __init__(self, modell, marke, preis, gepaecktraeger):
        super().__init__(modell, marke, preis, 20)
        self.gepaecktraeger = gepaecktraeger