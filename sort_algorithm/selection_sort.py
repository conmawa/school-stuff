from random import randint

def selection_sort(array):
    # Wiederhole so oft, wie die Liste lang ist
    for i in range(len(lst)):
        # kleinster Index wird auf i gesetzt
        min_idx = i
        # Wiederhole von i+1 bis Anzahl der Elemente in Liste
        for j in range(i + 1, len(lst)):
            # Überprüfe ob Element an Stelle kleinster Index größer als Element an Stelle j ist
            if array[min_idx] > array[j]: # -> wahr
                # setzte kleinsten Index auf j
                min_idx = j
        # Tausche Element an Stelle i mit Element an Stelle kleinster Index
        array[i], array[min_idx] = array[min_idx], array[i]
    return array

lst = []
for i in range(10):
    lst.append(randint(0,100))
               
print(lst)
print(selection_sort(lst))