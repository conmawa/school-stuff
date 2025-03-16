class Ordner:
    def __init__(self, name, speicher = 0):
        self.name = name
        self.speichergroesse = speicher
        self.unterordner = []
    
    def ordner_hinzufuegen(self, neuer_ordner):
        self.unterordner.append(neuer_ordner)
    
class Laufwerk:
    def __init__(self, name_laufwerk):
        self.name = name_laufwerk
        self.ordner = Ordner('root')
        
    def ordner_suchen(self, ordner_name, ordner = None):
        if ordner is None:
            ordner = self.ordner
        if ordner.name == ordner_name:
                return ordner
        for unterordner in ordner.unterordner:
            result = self.ordner_suchen(ordner_name, unterordner)
            if result:
                return result
        return None
    
    def ordner_hinzufuegen(self, parent_name, neuer_ordner):
        ordner = self.ordner_suchen(parent_name)
        if ordner:
            ordner.ordner_hinzufuegen(neuer_ordner)
    
    def struktur_anzeigen(self, ordner = None, ebene = 0):
        if ordner is None:
            ordner = self.ordner
        print(ebene * '--> ',ordner.name, ordner.speichergroesse, 'MB')
        for i in ordner.unterordner:
            self.struktur_anzeigen(i, ebene+1)
    
    def gesamt_groesse_berechnen(self, ordner = None):
        if ordner is None:
            ordner = self.ordner
        if len(ordner.unterordner) == 0:
            return ordner.speichergroesse
        speicher = ordner.speichergroesse
        for unterordner in ordner.unterordner:
            speicher += self.gesamt_groesse_berechnen(unterordner)
        return speicher
    
    def zip_ordner(self, ordner_name):
        ordner = self.ordner_suchen(ordner_name)
        if ordner:
            ordner.speichergroesse = ordner.speichergroesse / 2
            for unterordner in ordner.unterordner:
                self.zip_ordner(unterordner.name)
    
        
    
laufwerk = Laufwerk('C')
laufwerk.ordner_hinzufuegen('root', Ordner('Dokumente', 100))
laufwerk.ordner_hinzufuegen('root', Ordner('Musik', 200))
laufwerk.ordner_hinzufuegen('Musik', Ordner('Lieder', 150))
laufwerk.ordner_hinzufuegen('Dokumente', Ordner('Backup', 50))

laufwerk.struktur_anzeigen()

print(laufwerk.gesamt_groesse_berechnen())

laufwerk.zip_ordner('Musik')
laufwerk.struktur_anzeigen()
print(laufwerk.gesamt_groesse_berechnen())