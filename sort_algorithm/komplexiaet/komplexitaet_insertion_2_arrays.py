from random import randint
import matplotlib.pyplot as plt
from timeit import default_timer

def insertion_sort_2_arrays(unsorted_array, sorted_array):
    global time
    start = default_timer()
    sorted_array.append(unsorted_array[0])
    unsorted_array.pop(0)
    for i in range(len(unsorted_array)):
        zahl = unsorted_array[0]
        j = i
        while zahl < sorted_array[j] and j>=0:
            j -= 1
        sorted_array.insert(j+1, zahl)
        unsorted_array.pop(0)
    end = default_timer()
    time = end - start
    return sorted_array

x = 0
z = 10
anzahl = []
lst = []
s_lst = []
zeiten = []

while x < 15:
    for i in range(85*z):
        lst.append(randint(0,100))
    anzahl.append(len(lst))
    insertion_sort_2_arrays(lst, s_lst)
    zeiten.append(time)
    x += 1
    z += 5

plt.plot(anzahl, zeiten, marker="o", label="Insertion-Sort mit 2 Arrays")
plt.grid()
plt.title("Komplexität")
plt.xlabel("Listenlänge")
plt.ylabel("Zeit in s")
plt.legend(loc="upper left")
plt.minorticks_on()
plt.show()