from random import randint
import matplotlib.pyplot as plt
from timeit import default_timer


def selection_sort(array):
    global time
    start = default_timer()
    for i in range(len(lst)):
        min_idx = i
        for j in range(i + 1, len(lst)):
            if array[min_idx] > array[j]:
                min_idx = j
        array[i], array[min_idx] = array[min_idx], array[i]
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
    selection_sort(lst)
    zeiten.append(time)
    x += 1
    z += 5

plt.plot(anzahl, zeiten, marker="o", label="Selection-Sort")
plt.grid()
plt.title("Komplexität")
plt.xlabel("Listenlänge")
plt.ylabel("Zeit in s")
plt.legend(loc="upper left")
plt.minorticks_on()
plt.show()