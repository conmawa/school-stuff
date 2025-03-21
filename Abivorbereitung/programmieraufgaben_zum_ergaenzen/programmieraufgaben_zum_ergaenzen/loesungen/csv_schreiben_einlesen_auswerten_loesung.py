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
    werte = [eintrag[1] for eintrag in daten]  # Liste mit Zahlenwerten
    summe = sum(werte)
    durchschnitt = summe / len(werte) if werte else 0
    groesster_wert = max(werte) if werte else None

    print(f"Summe der Werte: {summe}")
    print(f"Durchschnitt: {durchschnitt:.2f}")
    print(f"Größter Wert: {groesster_wert}")

csv_auswerten(eingelesene_daten)
