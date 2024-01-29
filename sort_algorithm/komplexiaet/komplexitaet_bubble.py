from random import randint
import matplotlib.pyplot as plt
from timeit import default_timer

def bubble_sort(array):
    global time
    start = default_timer()
    for i in range(len(array) - 1):
        for c in range(len(array) - 1 - i):
            if array[c] > array[c+1]:
                array[c], array[c+1] = array[c+1], array[c]
    end = default_timer()
    time = end - start
    return time

x = 0
z = 10
anzahl = []
lst = []
zeiten = []

while x < 15:
    for i in range(10*z):
        lst.append(randint(0,100))
    anzahl.append(len(lst))
    bubble_sort(lst)
    zeiten.append(time)
    x += 1
    z += 5

plt.plot(anzahl, zeiten, marker="o", label="Bubble-Sort")
plt.grid()
plt.title("Komplexität")
plt.xlabel("Listenlänge")
plt.ylabel("Zeit in s")
plt.legend(loc="upper left")
plt.minorticks_on()
plt.show()