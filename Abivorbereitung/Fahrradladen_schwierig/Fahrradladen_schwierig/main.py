from fahrradladen import *
from kunden import *

laden = Fahrradladen()
citybike = laden.neues_fahrrad_hinzufuegen('Citybike', 'Cube', 500, True)
mountainbike = laden.neues_fahrrad_hinzufuegen('Mountainbike', 'Giant', 750, 'Vollfederung')
rennrad = laden.neues_fahrrad_hinzufuegen('Rennrad', 'Scott', 1500, 5)

kunde = Kunden('Bernd das Brot', 1)
laden.kunde_hinzufuegen(kunde)

def prozess():
    was = input('Möchtest du ein Fahrrad kaufen oder mieten? ').lower()
    welches = input('Welches Fahrrad möchtest du? (Citybike/Mountainbike/Rennrad) ').lower()
    if was == 'mieten':
        tage = int(input('Wie viele Tage möchtest du das Fahrrad mieten? '))
        if welches == 'citybike':
            preis = laden.fahrrad_vermieten(kunde, citybike, tage)
            print(citybike.marke, 'wurde gemietet; Preis beträgt ', preis, '€' )
        elif welches == 'mountainbike':
            preis = laden.fahrrad_vermieten(kunde, mountainbike, tage)
            print(mountainbike.marke, 'wurde gemietet; Preis beträgt ', preis, '€')
        elif welches == 'rennrad':
            preis = laden.fahrrad_vermieten(kunde, rennrad, tage)
            print(rennrad.marke, 'wurde gemietet; Preis beträgt ', preis, '€')
    else:
        if welches == 'citybike':
            preis = laden.fahrrad_verkaufen(kunde, citybike)
            print(citybike.marke, 'wurde gekauft für', preis, '€')
        elif welches == 'mountainbike':
            preis = laden.fahrrad_verkaufen(kunde, mountainbike)
            print(mountainbike.marke, 'wurde gekauft für', preis, '€')
        elif welches == 'rennrad':
            preis = laden.fahrrad_verkaufen(kunde, rennrad)
            print(rennrad.marke, 'wurde gekauft für', preis, '€')
weiter = True
while weiter != False:
    prozess()
    weiter = False if input('Beenden oder wieder zu 1.? ').lower() == 'beenden' else True
    
