from tier import *

class Pflanzenfresser(Tier):
    def __init__(self, name, art, gewicht):
        super().__init__(name, art, gewicht)
    
    def berechne_futtermenge(self):
        essen = {}
        essen['Fleisch'] = 0
        essen["Pflanzen"] = self.get_gewicht() * 0.3
        essen['Fisch'] = 0
        return essen