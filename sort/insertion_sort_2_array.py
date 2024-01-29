from random import randint

def insertion_sort_2_arrays(unsorted_array, sorted_array):
    # füge in sortierter Liste das 1. (also Stelle 0) Element aus der unsortierten Liste ein
    sorted_array.append(unsorted_array[0])
    # enferne das 1. Element aus der unsortierten Liste
    unsorted_array.pop(0)
    # Wiederhole die Anzahl an Listen Elementen der unsortierten Liste
    for i in range(len(unsorted_array)):
        # setze zahl auf das 1. Element der unsortierten Liste
        zahl = unsorted_array[0]
        # setze j auf i
        j = i
        # Wiederhole solange die zahl kleiner ist als das Element an der Stelle j der unsortierten Liste
        # UND solange j größer-gleich als 0 ist
        while zahl < sorted_array[j] and j>=0:
            # verringere j um ein
            j -= 1
        # füge an der Stelle j+1  die zahl in die sortierte Liste ein
        sorted_array.insert(j+1, zahl)
        # lösche das erste Element aus der unsortierten Liste
        unsorted_array.pop(0)
    return sorted_array

unsorted_lst = []
sorted_lst = []
for i in range (10):
    unsorted_lst.append(randint(0,100))

print(unsorted_lst)   
print(insertion_sort_2_arrays(unsorted_lst, sorted_lst))
