## Aufgabe von ChatGPT ##

from abc import ABC, abstractmethod
from math import *

class Form(ABC):
    @abstractmethod
    def bereche_flaeche(self):
        pass
    
class Rechteck(Form):
    def __init__(self, hoehe, breite):
        self.hoehe = hoehe
        self.breite = breite
        
    def bereche_flaeche(self):
        return self.hoehe * self.breite

class Kreis(Form):
    def __init__(self, radius):
        self.radius = radius
        
    def bereche_flaeche(self):
        return pi * self.radius**2

rechteck = Rechteck(100,2)
print(rechteck.bereche_flaeche())

kreis = Kreis(10)
print(kreis.bereche_flaeche())