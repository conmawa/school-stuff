from citybike import *
from mountainbike import *
from rennrad import *

class Fahrradladen:
    def __init__(self):
        self.bestand = []
        self.kunden = []
    
    def neues_fahrrad_hinzufuegen(self, modell, marke, preis, sonder_merkmal):
        if modell.lower() == 'citybike':
            gepaecktraeger = sonder_merkmal
            fahrrad = Citybike(modell, marke, preis, gepaecktraeger)
            self.bestand.append(fahrrad)
            return fahrrad
        elif modell.lower() == 'mountainbike':
            federung = sonder_merkmal
            fahrrad = Mountainbike(modell, marke, preis, federung)
            self.bestand.append(fahrrad)
            return fahrrad
        elif modell.lower() == 'rennrad':
            gewicht = sonder_merkmal
            fahrrad = Rennrad(modell, marke, preis, gewicht)
            self.bestand.append(fahrrad)
            return fahrrad
        else:
            print('falscher typ')
    
    def fahrrad_verkaufen(self, kunde, fahrrad):
        if kunde in self.kunden:
            kunde.kaufe_fahrrad(fahrrad)
            self.bestand.remove(fahrrad)
            return fahrrad.preis
        else:
            print('Kunde nicht vorhanden')
    
    def fahrrad_vermieten(self, kunde, fahrrad, tage):
        if kunde in self.kunden:
            kunde.miete_fahrrad(fahrrad)
            fahrrad.verfuegbar = False
            preis = fahrrad.berechne_mietkosten(tage)
            return preis
        else:
            print('Kunde nicht vorhanden')
    
    def fahrrad_zurueckgeben(self, kunde, tage_zu_spaet = None):
        if kunde == kunde:
            preis = kunde.rueckgabe_fahrrad(fahrrad, tage_zu_spaet)
            fahrrad.verfuegbar = True
            if preis != 0:
                print(preis, '€ müssen nachgezahlt werden')
        else:
            print('Kunde nicht vorhanden')
        
    def kunde_hinzufuegen(self, kunde):
        self.kunden.append(kunde)