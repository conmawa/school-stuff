# Comb Sort Algorithmus
# ----------------------
# Comb Sort ist eine Verbesserung des Bubble Sort. Er reduziert das Problem des "Turtling"
# (kleine Elemente am Ende der Liste, die sich nur langsam nach vorne bewegen).
# Anstatt benachbarte Elemente zu vergleichen, nutzt Comb Sort einen variablen Abstand ("gap"),
# um Elemente weiter entfernt zu vergleichen und zu tauschen.
# Dieser Abstand beginnt mit der Länge der Liste und wird in jedem Durchlauf verkleinert.
# Am Ende verhält sich Comb Sort ähnlich wie Bubble Sort, führt aber weniger Vergleiche aus.

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
            if liste[i] > liste[i + gap]:  # Falls das linke Element größer ist als das rechte
                liste[i], liste[i + gap] = liste[i + gap], liste[i]  # Tausche die Elemente
                fertig = False  # Falls ein Tausch passiert, ist die Liste noch nicht fertig sortiert
            i += 1  # Zum nächsten Element gehen

# Test
zahlen = [8, 4, 1, 7, 3, 9, 5]
comb_sort(zahlen)
print(zahlen)  # Erwartete Ausgabe: [1, 3, 4, 5, 7, 8, 9]
