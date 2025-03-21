# Merge Sort Algorithmus
# ----------------------
# Merge Sort ist ein "Teile-und-Herrsche"-Algorithmus.
# Die Liste wird in zwei Hälften geteilt, sortiert und anschließend wieder zusammengeführt.

# Aufgabe: Implementiere die fehlende Merge-Funktion!
# Die Funktion soll zwei sortierte Listen zu einer neuen, sortierten Liste zusammenführen.

def merge_sort(liste):
    if len(liste) <= 1:  # Falls die Liste nur ein Element hat, ist sie bereits sortiert
        return liste  

    mitte = len(liste) // 2  # Die Mitte der Liste finden
    linke_haelfte = merge_sort(liste[:mitte])  # Linke Hälfte sortieren (rekursiv)
    rechte_haelfte = merge_sort(liste[mitte:])  # Rechte Hälfte sortieren (rekursiv)

    return merge(linke_haelfte, rechte_haelfte)  # Sortierte Hälften zusammenführen

def merge(linke, rechte):
    ergebnis = []  # Neue Liste für das zusammengeführte Ergebnis
    i, j = 0, 0  # Zeiger für linke und rechte Liste

    # TODO: Implementiere hier die Merge-Logik!
    # Solange beide Listen noch Elemente haben:
    #     - Vergleiche die aktuellen Elemente der beiden Listen
    #     - Füge das kleinere Element zur Ergebnisliste hinzu
    #     - Verschiebe den Zeiger der Liste, aus der das Element genommen wurde
    # Falls noch Elemente in einer der Listen übrig sind:
    #     - Hänge alle verbleibenden Elemente der Ergebnisliste an
    
    return ergebnis

# Test
zahlen = [8, 3, 5, 1, 9, 6, 2, 7, 4]
sortierte_zahlen = merge_sort(zahlen)
print(sortierte_zahlen)  # Erwartete Ausgabe: [1, 2, 3, 4, 5, 6, 7, 8, 9]
