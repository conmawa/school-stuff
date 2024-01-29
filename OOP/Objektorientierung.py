# Objektorientierte Programmierung

# zahl = 1
# text = "hallo"
# float = 3.2

# print(type(zahl))
# print(type(text))
# print(type(float))

# neu = zahl + text # --> Fehler, da zwei Klassen


# liste = [2,1,3,5]
# print(type(liste))
# liste.append(6) # Funktionen, die in einer Klasse gelten => Methoden

# zahl = 5
# zahl.append(4) # --> Fehler, da keine Funktion für Klasse 'int'


#####################################
# Eigene Klasse definieren #

class Hund: # immer mit Großbuchstaben beginnen
    # Attribute #
    def __init__(self, name): # Init-Methode wird beim Anlegen eines Objekts ausgeführt (Konstruktor)
        self.name = name
    
    # Methode #
    def bellen(self): # self ist das Objekt selbst
        print("Wau Wau")
        
hund1 = Hund("rex") # --> eine Instanz der Klasse Hund erzeugt -> Objekt
#print(type(hund1))

print(hund1.name)

hund1.bellen()

hund2 = Hund("balu")
print(hund2.name)
hund2.bellen()






