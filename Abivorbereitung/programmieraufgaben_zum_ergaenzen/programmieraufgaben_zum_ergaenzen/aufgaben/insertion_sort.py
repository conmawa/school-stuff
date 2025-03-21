# Insertion Sort Algorithmus
# ----------------------
# Insertion Sort funktioniert, indem Elemente nacheinander an die richtige Stelle eingefügt werden.
# Dabei werden größere Werte nach rechts verschoben, bis Platz für das aktuelle Element ist.

# Aufgabe: Implementiere die fehlende Logik für das Verschieben der Elemente!
# Die Funktion soll eine Liste von Zahlen aufsteigend sortieren.

def insertion_sort(liste):
    for i in range(1, len(liste)):  # Starte mit dem zweiten Element
        schluessel = liste[i]  # Das aktuelle Element merken
        j = i - 1  # Index des vorherigen Elements

        # TODO: Implementiere hier die Verschiebe-Logik!
        # Solange das vorherige Element größer ist:
        #     - Schiebe das größere Element nach rechts
        #     - Bewege den Index zurück
        
        liste[j + 1] = schluessel  # Setze das aktuelle Element an die richtige Stelle

# Test
zahlen = [5, 3, 8, 4, 2]
insertion_sort(zahlen)
print(zahlen)  # Erwartete Ausgabe: [2, 3, 4, 5, 8]
