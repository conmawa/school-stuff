## Assoziation und Aggregation ##

class Fahrer:
    def __init__(self, name):
        self.name = name

class Reifen:
    def __init__(self, typ):
        self.typ = typ
        
class Auto:
    def __init__(self, modell, fahrer):
        self.modell = modell
        self.fahrer = Fahrer(fahrer)  # Assoziation # Erstellung eines Objektes für die Klasse Fahrer
        self.reifen = [Reifen("Winter - Links"), Reifen("Winter - Links"), Reifen("Winter - Rechts"), Reifen("Winter - Rechts")]  # Aggregation # Erstellung einer Liste, wo jedes Element ein Objekt der Klasse Reifen ist
        
auto = Auto("Tesla", "Mike")
for i in range(4):
    print(auto.reifen[i].typ) # daher muss man zusätlich bei der Liste reifen an der Stelle 0 noch auch das Attribut typ zugreifen
print(auto.modell)
print(auto.fahrer.name) # bzw. hier noch auf das Attribut Name auf das Objekt fahrer auf das Objekt auto zugreifen