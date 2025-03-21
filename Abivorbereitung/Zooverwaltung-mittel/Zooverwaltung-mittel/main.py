from fleischfresser import Fleischfresser
from pflanzenfresser import Pflanzenfresser
from allesfresser import Allesfresser
from fischfresser import Fischfresser

class Main():
    def __init__(self):
        self.tiere = []
    
    def add_tier(self, name, art, gewicht):
        if art.lower() == "fleischfresser":
            tier = Fleischfresser(name, art, gewicht)
        elif art.lower() == "pflanzenfresser":
            tier = Pflanzenfresser(name, art, gewicht)
        elif art.lower() == "allesfresser":
            tier = Allesfresser(name, art, gewicht)
        elif art.lower() == "fischfresser":
            tier = Fischfresser(name, art, gewicht)
        else:
            return None
        self.tiere.append({'Tier': tier, 'Futterbedarf': tier.berechne_futtermenge()})
    
    def tier_fuetter(self, tier):
        print(tier.berechne_futtermenge())
    
    def ausgeben(self):
        for eintrag in self.tiere:
            print('Name: ', eintrag['Tier'].get_name(), '; Art: ',  eintrag['Tier'].get_art(), '; Gewicht: ', eintrag['Tier'].get_gewicht(), 'kg; Futterbedarf Fleisch: ', eintrag['Futterbedarf']['Fleisch'], 'kg; Futterbedarf Pflanzen: ', eintrag['Futterbedarf']['Pflanzen'], 'kg; Futterbedarf Fisch: ',eintrag['Futterbedarf']['Fisch'], 'kg')

zoo = Main()
zoo.add_tier("Löwe", "Fleischfresser", 10)
zoo.add_tier("Elefant", "Pflanzenfresser", 50)
zoo.add_tier("Papagei", "Allesfresser", 100)
zoo.add_tier("Pinguin", "Fischfresser", 20)

for eintrag in zoo.tiere:
    zoo.tier_fuetter(eintrag['Tier'])

zoo.ausgeben()