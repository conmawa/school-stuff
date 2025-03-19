from tier import *

class Fleischfresser(Tier):
    def __init__(self, name, art, gewicht):
        super().__init__(name, art, gewicht)
    
    def berechne_futtermenge(self):
        essen = {}
        essen["Fleisch"] = self.get_gewicht() * 0.1
        essen["Pflanzen"] = 0
        essen["Fisch"] = 0
        return essen