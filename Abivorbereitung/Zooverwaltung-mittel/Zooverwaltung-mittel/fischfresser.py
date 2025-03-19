from tier import *

class Fischfresser(Tier):
    def __init__(self, name, art, gewicht):
        super().__init__(name, art, gewicht)
    
    def berechne_futtermenge(self):
        essen = {}
        essen['Fleisch'] = 0
        essen["Pflanzen"] = 0
        essen["Fisch"] = self.get_gewicht() * 0.2
        return essen