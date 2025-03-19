from tier import *

class Allesfresser(Tier):
    def __init__(self, name, art, gewicht):
        super().__init__(name, art, gewicht)
    
    def berechne_futtermenge(self):
        essen = {}
        essen["Fleisch"] = self.get_gewicht() * 0.1
        essen["Pflanzen"] = self.get_gewicht() * 0.25
        essen['Fisch'] = 0
        return essen