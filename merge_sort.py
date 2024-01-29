from random import randint

def merge_sort(array):
    # Überprüfung ob Länge der Liste größer 1 ist
    if len(array) > 1:
        # Länge der Liste wird durch 2 geteilt und abgerundet
        half = len(array) // 2
        # neues Liste mit linkem Teil
        left_array = array[:half]
        # neues Liste mit rechtem Teil
        right_array = array[half:]
        
        # linke Liste noch einmal teilen
        merge_sort(left_array)
        # rechte Liste noch einmal teilen
        merge_sort(right_array)
        
        # i = Index für linke Liste
        # j = Index für rechte Liste
        # k = Index für sortierte Liste
        i = j = k = 0
        # arbeite solange i kleiner als Länge von linker Liste und j kleiner als Länge von rechter Liste
        while i < len(left_array) and j < len(right_array):
            # linke Liste an Stelle i kleiner als rechte Liste an Stelle j?
            if left_array[i] < right_array[j]: # -> Ja
                # sortierte Liste an der Stelle k wird auf die linke Liste der Stelle i gesetzt
                array[k] = left_array[i]
                # i wird um eins erhöht
                i += 1
            else: # -> Nein
                # sortierte Liste an der Stelle k wird auf die rechte Liste der Stelle j gesetzt
                array[k] = right_array[j]
                # j wird um eins erhöht
                j += 1
            # k wird um eins erhöht
            k += 1
        # arbeite solange i kleiner als die Länge der linken Liste ist
        while i < len(left_array):
            # sortierte Liste an Stelle k wird auf die Linke Liste an der Stelle i gestezt
            array[k] = left_array[i]
            # erhöhe i um eins
            i += 1
            # erhöhe k um eins
            k += 1
        # arbeite solange j kleiner als die Länge der rechten Liste ist
        while j < len(right_array):
            # sortierte Liste an Stelle k wird auf die rechete Liste an der Stelle j gestezt
            array[k] = right_array[j]
            # erhöhe j um eins
            j += 1
            # erhöhe k um eins
            k += 1
    return array      

lst = []
for i in range(10):
    lst.append(randint(0,100))

print(merge_sort(lst))