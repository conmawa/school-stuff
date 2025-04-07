# Insertion Sort Algorithmus
# ----------------------
# Insertion Sort ist ein einfacher Sortieralgorithmus, der ähnlich wie das Einfügen von Spielkarten
# in eine sortierte Hand funktioniert. Elemente werden nacheinander aus der unsortierten Liste
# genommen und an die richtige Stelle in der bereits sortierten Liste eingefügt.
# 
# Ablauf:
# 1. Beginne mit dem zweiten Element, weil das erste alleine schon sortiert ist.
# 2. Vergleiche es mit den vorherigen Elementen und schiebe größere Elemente nach rechts.
# 3. Setze das aktuelle Element an die richtige Stelle.
# 4. Wiederhole diesen Vorgang für jedes weitere Element.

def insertion_sort(liste):
    for i in range(1, len(liste)):  # Starte mit dem zweiten Element
        schluessel = liste[i]  # Das aktuelle Element merken
        j = i - 1  # Index des vorherigen Elements

        while j >= 0 and liste[j] > schluessel:  # Solange das vorherige Element größer ist
            liste[j + 1] = liste[j]  # Schiebe das größere Element nach rechts
            j -= 1  # Gehe ein Element weiter zurück
        
        liste[j + 1] = schluessel  # Setze das aktuelle Element an die richtige Stelle

# Test
zahlen = [5, 3, 8, 4, 2]
insertion_sort(zahlen)
print(zahlen)  # Erwartete Ausgabe: [2, 3, 4, 5, 8]
