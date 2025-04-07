class Automat:
    def __init__(self): #"""Initialisiert eine leere Produktliste."""
        self.produkte = self.generiere_produkte()
    
    def produkt_kategorie(self):
        return "Allgemein"

    def ist_gueltiger_code(self, produktcode): # --> am besten lösen mit einer rekursiven Funktion um Code durchzugehen und zu schauen ob er nur aus G und S bzw. Ziffern besteht
        if produktcode in [0] == G or [0] == S # Überprüft ob Produktcode mit G oder S beginnt --> brauch noch kontrolle ob nur zahlen danach kommen
            return True
        else:
            return False
        
        for produktcode[1].isdigit() and for produktcoe[2].isdigit():
            retrurn True
        
        
    
    def verkauf_durchfuehren(self, produktcode): #"""Überprüft, ob ein Produktcode gültig ist und gibt eine Meldung aus."""
        if self.ist_gueltiger_code(produktcode) and produktcode in self.produkte:
            print(f"{self.produkt_kategorie()} verkauft: {produktcode}")
        else:
            print("Ungültiger Produktcode oder Produkt nicht verfügbar.")

    def zeige_produkte(self): #"""Zeigt die verfügbaren Produkte im Automaten."""
        print(f"Produkte im {self.produkt_kategorie()}-Automaten:")
        for produkt in self.produkte:
            print(produkt)

    def generiere_produkte(self):
        """Soll in Unterklassen überschrieben werden."""
        return []


#ToDo: Klasse Snackautomat
class Snackautomat:
    def __init__(self)

# -----------------------------------------------
# TESTBEREICH

def verkaufs_simulation(automat, produktcode):
    """Simuliert einen Verkauf an einem beliebigen Automaten."""
    automat.verkauf_durchfuehren(produktcode)

### Tests ###
# snackautomat = SnackAutomat()
# 
# print("\n--- VERFÜGBARE PRODUKTE ---\n")
# snackautomat.zeige_produkte()
# 
# print("\n--- TESTS BEGINNEN ---\n")
# verkaufs_simulation(snackautomat, "S31")
# verkaufs_simulation(snackautomat, "G99")
# print("\n--- TESTS BEENDET ---\n")
