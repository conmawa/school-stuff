class Mensch:
    def __init__(self, name):
        self.name = name

class Reifen:
    def __init__(self, typ):
        self.typ = typ

class Gangschaltung:
    def __init__(self, typ):
        self.typ = typ  # Zum Beispiel "manuell" oder "automatisch"

class Scheibenwischer:
    def __init__(self, laenge):
        self.laenge = laenge  # Länge der Scheibenwischer in cm

class Auto:
    def __init__(self, modell, fahrer):
        self.modell = modell
        self.fahrer = fahrer  # Assoziation - Hier muss ein Objekt der Klasse "Mensch" übergeben werden
        self.reifen = [Reifen("Winter - Vorne Links"), Reifen("Winter - Hinten Links"), Reifen("Winter - Vorne Rechts"), Reifen("Winter - Hinten Rechts")]  # Aggregation
        self.gangschaltung = Gangschaltung("manuell")  # Komposition - Das Auto "besitzt" eine Gangschaltung, die spezifisch für das Auto konzipiert ist
        self.scheibenwischer = Scheibenwischer(50)  # Komposition - Das Auto "besitzt" Scheibenwischer, die ohne das Auto nicht ihre Funktion erfüllen können
        
mensch1 = Mensch("Ralf")

auto = Auto("Toyota", mensch1)

print(auto.fahrer.name)
print(auto.modell)
for i in range(len(auto.reifen)):
    print(auto.reifen[i].typ)
print(auto.gangschaltung.typ)
print(auto.scheibenwischer.laenge)