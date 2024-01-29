from random import randint

def bubble_sort(array):
    # Wiederhole Anzahl der Elemente in der Liste
    for i in range(len(lst)):
        # Wiederhole Anzahl der Elemente in der Liste - 1
        for i in range(len(lst) - 1):
            # Überprüfe ob Liste ab Stelle i ist größer als Liste an Stelle i+1
            if array[i] > array[i+1]:
                # setze eine temporäre Variable auf Listenelement an der Stelle i
                temp = array[i]
                # setze Listenelemnt an der Stelle i auf Element der Stelle i+1
                array[i] = array[i+1]
                # steze Listenelement an der Stelle i+1 auf die temporäre Varibale
                array[i+1] = temp
    return array
lst = []
for i in range(10):
    lst.append(randint(0,100))

print(lst)
print(bubble_sort(lst))