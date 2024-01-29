from random import randint
import matplotlib.pyplot as plt
from timeit import default_timer

def merge_sort(array):
    global start, ende, calc_time
    start = default_timer()
    
    if len(array) > 1:
        half = len(array) // 2
        left_array = array[:half]
        right_array = array[half:]
        
        merge_sort(left_array)
        merge_sort(right_array)
        
        i = j = k = 0
        while i < len(left_array) and j < len(right_array):
            if left_array[i] < right_array[j]:
                array[k] = left_array[i]
                i += 1
            else:
                array[k] = right_array[j]
                j += 1
            k += 1
        while i < len(left_array):
            array[k] = left_array[i]
            i += 1
            k += 1
        while j < len(right_array):
            array[k] = right_array[j]
            j += 1
            k += 1
    
    ende = default_timer()
    calc_time = (ende - start) 
    return calc_time
        

lst = []
x = 0
z = 100
anzahl = []
zeiten = []

while x < 15:
    for i in range(1000*z):
        lst.append(randint(0,100000))
    anzahl.append(len(lst))
    sorted_array = merge_sort(lst)
    zeiten.append(calc_time)
    x += 1
    z += 100


plt.plot(anzahl, zeiten, label="Merge-Sort", marker="o")
plt.title("Komplexität")
plt.xlabel("Listenlänge")
plt.ylabel("Zeit in s")
plt.legend(loc="upper left")
plt.grid(which='major', color='black', linewidth=1)
plt.grid(which='minor', color='gray', linewidth=0.5)
plt.minorticks_on()
plt.show()