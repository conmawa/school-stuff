from random import randint
from matplotlib import pyplot as plt
from timeit import default_timer

def heap_sort(array):
    global time
    start = default_timer()
    for i in range(len(array)//2-1, 0, -1):
        heapify(array, len(array), i)
        
    
    for i in range(len(array)-1, 0, -1):
        array[0], array[i] = array[i], array[0]
        
        heapify(array, i, 0)
    end = default_timer()
    time = end - start

def heapify(array, size, w_index):
    biggest = w_index
    left = 2 * w_index + 1
    right = 2 * w_index + 2
    
    if left < size and array[left] > array[biggest]:
        biggest = left
        
    if right < size and array[right] > array[biggest]:
        biggest = right
    
    if biggest != w_index:
        array[w_index], array[biggest] = array[biggest], array[w_index]
        heapify(array, size, biggest)
        


x = 0
z = 10
anzahl = []
lst = []
zeiten = []

while x < 40:
    for i in range(50*z):
        lst.append(randint(0,1000))
    anzahl.append(len(lst))
    heap_sort(lst)
    zeiten.append(time)
    x += 1
    z += 5

plt.plot(anzahl, zeiten, marker="o", label="Heap-Sort")
plt.grid()
plt.title("Komplexität")
plt.xlabel("Listenlänge")
plt.ylabel("Zeit in s")
plt.legend(loc="upper left")
plt.minorticks_on()
plt.show()
