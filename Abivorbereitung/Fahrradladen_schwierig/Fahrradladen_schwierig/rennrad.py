from fahrrad import *

class Rennrad(Fahrrad):
    def __init__(self, modell, marke, preis, gewicht):
        super().__init__(modell, marke, preis, 50)
        self.gewicht = gewicht

