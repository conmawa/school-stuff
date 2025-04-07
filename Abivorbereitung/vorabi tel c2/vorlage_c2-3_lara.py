class Automat:
    """Basisklasse für Verkaufsautomaten."""

    def __init__(self):
        """Initialisiert eine leere Produktliste."""
        self.produkte = self.generiere_produkte()
    
    def produkt_kategorie(self):
        return "Allgemein"

    def ist_gueltiger_code(self, produktcode):
        """ToDo: Überprüft, ob der Produktcode gültig ist."""
        pass
    
    def verkauf_durchfuehren(self, produktcode):
        """Überprüft, ob ein Produktcode gültig ist und gibt eine Meldung aus."""
        if self.ist_gueltiger_code(produktcode) and produktcode in self.produkte:
            print(f"{self.produkt_kategorie()} verkauft: {produktcode}")
        else:
            print("Ungültiger Produktcode oder Produkt nicht verfügbar.")

    def zeige_produkte(self):
        """Zeigt die verfügbaren Produkte im Automaten."""
        print(f"Produkte im {self.produkt_kategorie()}-Automaten:")
        for produkt in self.produkte:
            print(produkt)

    def generiere_produkte(self):
        """Soll in Unterklassen überschrieben werden."""
        return []


#ToDo: Klasse Snackautomat
class SnackAutomat(Automat):
    def __init__(self):
        super().__init__()
    
    def produkt_kategorie(self):
        return "Snack"
    
    def ist_gueltiger_code(self, produktcode):
        produktcode = list(produktcode)
        if produktcode[0] == 'S' and produktcode[1].isdigit() and produktcode[2].isdigit():
            return True
        else:
            return False
    
    def generiere_produkte(self):
        return ['S10', 'S31', 'S32', 'S43', 'S54', 'S65', 'S76', 'S87', 'S98', 'S99']
        

# -----------------------------------------------
# TESTBEREICH

def verkaufs_simulation(automat, produktcode):
    """Simuliert einen Verkauf an einem beliebigen Automaten."""
    automat.verkauf_durchfuehren(produktcode)

### Tests ###
snackautomat = SnackAutomat()

print("\n--- VERFÜGBARE PRODUKTE ---\n")
snackautomat.zeige_produkte()
 
print("\n--- TESTS BEGINNEN ---\n")
verkaufs_simulation(snackautomat, "S31")
verkaufs_simulation(snackautomat, "G99")
print("\n--- TESTS BEENDET ---\n")
