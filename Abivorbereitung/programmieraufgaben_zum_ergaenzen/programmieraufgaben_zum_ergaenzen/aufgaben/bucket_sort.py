# Bucket Sort Algorithmus für ganze Zahlen
# ---------------------------------------
# Bucket Sort ist ein Sortierverfahren, das Zahlen in Gruppen (Buckets) verteilt,
# diese sortiert und dann alle Buckets zusammenfügt.
#
# Ablauf:
# 1. **Min und Max bestimmen**: Ermittle den kleinsten und größten Wert in der Liste.
# 2. **Buckets erstellen**: Erzeuge mehrere leere Buckets.
# 3. **Zahlen einsortieren**: Weise jeder Zahl anhand ihrer Position im Zahlenbereich einen Bucket zu.
# 4. **Buckets sortieren**: Sortiere jeden einzelnen Bucket mit einer Sortiermethode (z. B. Insertion Sort).
# 5. **Buckets zusammenfügen**: Füge alle sortierten Buckets zu einer finalen Liste zusammen.

#
# Aufgabe:
# Implementiere die fehlende Sortierlogik in Schritt 4!
# Jeder Bucket muss mit einer Sortiermethode sortiert werden.

def bucket_sort(liste):
    if len(liste) == 0:
        return liste  # Falls die Liste leer ist, sofort zurückgeben

    # 1. Bestimme den kleinsten und größten Wert
    min_wert = min(liste)
    max_wert = max(liste)

    # 2. Erstelle Buckets
    anzahl_buckets = len(liste)
    buckets = []
    for i in range(anzahl_buckets):
        buckets.append([])  # Füge eine leere Liste für jeden Bucket hinzu

    # 3. Zahlen in Buckets einsortieren
    for zahl in liste:
        index = int((zahl - min_wert) / (max_wert - min_wert) * (anzahl_buckets - 1))
        buckets[index].append(zahl)        
        
    # 4. Jeden Bucket sortieren (TODO: Hier fehlt die Sortierlogik!)
    for i in range(anzahl_buckets):
        buckets[i].sort()
    # Gehe durch jeden Bucket:
    #     - Sortiere den Bucket mit einer einfachen Methode

    # 5. Alle Buckets in eine sortierte Liste zusammenfügen
    sortierte_liste = []
    for i in range(anzahl_buckets):
        for zahl in buckets[i]:
            sortierte_liste.append(zahl)

    return sortierte_liste

# Test mit ganzen Zahlen
zahlen = [78, 17, 39, 26, 72, 94, 21, 12, 23, 68]
sortierte_zahlen = bucket_sort(zahlen)
print("Sortierte Zahlen:", sortierte_zahlen)
# Erwartete Ausgabe: [12, 17, 21, 23, 26, 39, 68, 72, 78, 94]
