# Merge Sort Algorithmus
# ----------------------
# Merge Sort ist ein rekursiver "Teile-und-Herrsche"-Algorithmus.
# Er teilt die Liste immer wieder in zwei Hälften, bis jede Hälfte nur noch ein Element enthält.
# Danach werden die kleinen sortierten Listen schrittweise zusammengeführt (merge),
# wobei jeweils die kleineren Elemente zuerst eingefügt werden.

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

    while i < len(linke) and j < len(rechte):  # Solange beide Listen noch Elemente haben
        if linke[i] < rechte[j]:  # Kleineres Element zuerst einfügen
            ergebnis.append(linke[i])
            i += 1  # Linke Liste weiter durchsuchen
        else:
            ergebnis.append(rechte[j])
            j += 1  # Rechte Liste weiter durchsuchen

    # Falls noch Elemente in einer der Listen übrig sind, anhängen
    ergebnis.extend(linke[i:])
    ergebnis.extend(rechte[j:])
    
    return ergebnis

# Test
zahlen = [8, 3, 5, 1, 9, 6, 2, 7, 4]
sortierte_zahlen = merge_sort(zahlen)
print(sortierte_zahlen)  # Erwartete Ausgabe: [1, 2, 3, 4, 5, 6, 7, 8, 9]
