from random import randint
import matplotlib.pyplot as plt
from timeit import default_timer

def insertion_sort(array):
    global time
    start = default_timer()
    for i in range(1, len(array)):
        index = array[i]
        j = i-1
        while j >= 0 and index < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = index
    end = default_timer()
    time = end - start
    return array

x = 0
z = 10
anzahl = []
lst = []
zeiten = []

while x < 15:
    for i in range(10*z):
        lst.append(randint(0,100))
    anzahl.append(len(lst))
    insertion_sort(lst)
    zeiten.append(time)
    x += 1
    z += 5

plt.plot(anzahl, zeiten, marker="o", label="Insertion-Sort")
plt.grid()
plt.title("Komplexität")
plt.xlabel("Listenlänge")
plt.ylabel("Zeit in s")
plt.legend(loc="upper left")
plt.minorticks_on()
plt.show()