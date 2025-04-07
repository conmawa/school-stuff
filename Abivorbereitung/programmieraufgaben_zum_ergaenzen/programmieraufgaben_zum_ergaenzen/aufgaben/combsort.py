# Comb Sort Algorithmus
# ----------------------
# Comb Sort verbessert den Bubble Sort, indem er mit einem variablen Abstand ("gap") arbeitet.
# Statt nur benachbarte Elemente zu vergleichen, werden weiter entfernte verglichen.
# Der Abstand beginnt groß und wird in jedem Durchlauf verkleinert.
# Dadurch werden große Werte schneller nach hinten verschoben, was die Sortierzeit verbessert.

# Aufgabe: Implementiere die fehlende Tausch-Logik!
# Die Funktion soll eine Liste von Zahlen aufsteigend sortieren.

def comb_sort(liste):
    gap = len(liste)  # Startabstand (gap) ist die Länge der Liste
    shrink = 1.3  # Der Abstand wird pro Durchgang durch diesen Faktor geteilt
    fertig = False  # Diese Variable wird True, wenn die Liste sortiert ist

    while not fertig:
        gap = int(gap / shrink)  # Abstand verkleinern
        if gap <= 1:  # Falls der Abstand kleiner als 1 wird, setzen wir ihn auf 1
            gap = 1
            fertig = True  # Erst annehmen, dass die Liste sortiert ist

        i = 0
        while i + gap < len(liste):  # Vergleiche Elemente mit Abstand "gap"
            if liste[i] > liste[i + gap]:
                liste[i], liste[i + gap] = liste[i + gap], liste[i]
                fertig = False
            # TODO: Überprüfe, ob ein Tausch nötig ist
            # Falls liste[i] größer ist als liste[i + gap]:
            #     - Tausche die beiden Elemente
            #     - Setze "fertig" auf False (weil die Liste möglicherweise noch nicht fertig sortiert ist)
            i += 1  # Zum nächsten Element gehen

# Test
zahlen = [8, 4, 1, 7, 3, 9, 5]
comb_sort(zahlen)
print(zahlen)  # Erwartete Ausgabe: [1, 3, 4, 5, 7, 8, 9]
