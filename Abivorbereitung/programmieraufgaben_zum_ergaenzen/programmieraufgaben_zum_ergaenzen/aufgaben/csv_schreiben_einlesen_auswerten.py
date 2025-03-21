# CSV-Datei erstellen, einlesen und auswerten
# -------------------------------------------
# 1. Erstellt eine CSV-Datei mit zwei Spalten: "Name" und "Wert".
# 2. Liest die CSV-Datei mit der csv-Bibliothek ein.
# 3. Wertet die Daten aus (Summe, Durchschnitt, größter Wert).

import csv

# Dateiname
datei_name = "daten.csv"

# Beispiel-Daten für die CSV
daten = [
    ["Apfel", 3],
    ["Banane", 5],
    ["Orange", 2],
    ["Kirsche", 7],
    ["Traube", 4]
]

# 1. CSV-Datei erstellen und speichern
def csv_erstellen(datei_name, daten):
    with open(datei_name, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Wert"])  # Spaltenüberschriften
        writer.writerows(daten)  # Daten in die Datei schreiben

csv_erstellen(datei_name, daten)
print(f"CSV-Datei '{datei_name}' wurde erstellt.")

# 2. CSV-Datei einlesen
def csv_einlesen(datei_name):
    daten = []
    with open(datei_name, mode="r", newline="") as file:
        reader = csv.reader(file)
        next(reader)  # Erste Zeile (Header) überspringen
        for row in reader:
            daten.append([row[0], int(row[1])])  # Name bleibt String, Wert wird Integer
    return daten

eingelesene_daten = csv_einlesen(datei_name)
print("Eingelesene Daten:", eingelesene_daten)

# 3. CSV-Daten auswerten
def csv_auswerten(daten):
    """Berechnet die Summe, den Durchschnitt und den größten Wert."""
    summe = 0
    max_wert = None
    anzahl = 0

    # TODO: Implementiere hier die Berechnungen!
    # - Erstelle eine Liste mit allen Werten aus `daten`
    # - Berechne die Summe aller Werte (`summe = ...`)
    # - Bestimme die Anzahl der Werte (`anzahl = ...`)
    # - Berechne den Durchschnitt (`durchschnitt = summe / anzahl`)
    # - Finde den größten Wert (`max_wert = ...`)

    print(f"Summe der Werte: {summe}")
    print(f"Durchschnitt: {0:.2f}")  # Hier sollte der berechnete Durchschnitt stehen
    print(f"Größter Wert: {max_wert}")

csv_auswerten(eingelesene_daten)
