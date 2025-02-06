def einlesen():
    with open('Abivorbereitung\zahlen.csv', "r") as file: # CSV-Datei einlesen
        zahlen = file.read().split("\n") # Zeilenweise trennen
        return zahlen
    
def even(binaer):
    if binaer[0] == '0': # erste Stelle gleich 0?
        integer = int(binaer, 2) # wenn ja, dann umwandeln
    else:
        integer = int(binaer, 2) - 256 # wenn nein, dann umwandeln und minus 256 rechnen
    
    if integer % 2 == 0: # gerade?
        return True

def positiv(binaer):
    return binaet[0] == '0'
    #zahl = list(binaer) # in Liste umwandeln
    #if zahl[0] == '0': # erste Stelle gleich 0?
    #    return True # wenn ja, dann positiv
    
def add_to_file(zahl):
    with open('Abivorbereitung\menge_c.csv', "w") as file:  # CSV-Datei schreiben
        file.write(zahl + "\n") # Zahl schreiben
    
def check():
    zahlen = einlesen() # Zahlen einlesen
    for zahl in zahlen: # für jede Zahl
        if even(zahl) and positiv(zahl): # wenn gerade und positiv
            add_to_file(zahl) # dann in Datei schreiben
          
check()
