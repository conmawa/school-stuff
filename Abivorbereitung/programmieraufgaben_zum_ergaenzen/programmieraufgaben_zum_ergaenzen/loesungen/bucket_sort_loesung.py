# Bucket Sort für ganze Zahlen (z. B. 10 bis 100)
# -----------------------------------------------
# Ablauf:
# 1. Bestimme den kleinsten und größten Wert.
# 2. Erstelle Buckets für den Zahlenbereich.
# 3. Weise jede Zahl dem passenden Bucket zu.
# 4. Sortiere jeden Bucket.
# 5. Verbinde die sortierten Buckets zu einer finalen Liste.

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
        buckets.append([])

    # 3. Zahlen in Buckets einsortieren
    for zahl in liste:
        index = int((zahl - min_wert) / (max_wert - min_wert) * (anzahl_buckets - 1))
        buckets[index].append(zahl)

    # 4. Jeden Bucket sortieren
    for i in range(anzahl_buckets):
        buckets[i].sort()

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
