from random import randint

def insertion_sort(array):
    # Wiederhole von 1 bis Länge der Liste
    for i in range(1, len(array)):
        # setze Index auf Element an Stelle i
        index = array[i]
        # setze j auf i-1
        j = i-1
        # Wiederhole solange j größer-gleich 0 ist UND index kleiner als Element an Stelle j
        while j >= 0 and index < array[j]:
            # setze Element an Stelle j+1 auf Element an der Stlle j
            array[j + 1] = array[j]
            # verkleinere j um eins
            j -= 1
        # setze Element an Stelle j+1 auf den Index
        array[j + 1] = index
    return array

lst = []
for i in range(10):
    lst.append(randint(0,100))

print(lst)    
print(insertion_sort(lst))