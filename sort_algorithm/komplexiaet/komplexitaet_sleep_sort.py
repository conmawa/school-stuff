from random import randint
import threading
from time import sleep
from timeit import default_timer
import matplotlib.pyplot as plt

def sleep_and_print(element):
    sleep(element)
    print(element, end = '')
    
    
def sleep_sort(array):
    global time
    
    start = default_timer()
    
    threads = []
    for element in array:
        thread = threading.Thread(target=sleep_and_print, args=(element,))
        threads.append(thread)
        thread.start()
        
    for thread in threads:
        thread.join()
        
    end = default_timer()
    time = end - start
    

lst = []
zeiten = []
anzahl = []
x = 0
z = 10

while x < 15:
    for i in range(10*z):
        lst.append(randint(0,100))
    anzahl.append(len(lst))
    sleep_sort(lst)
    zeiten.append(time)
    x += 1
    z += 5

plt.plot(anzahl, zeiten, marker="o", label="Sleep-Sort")
plt.grid()
plt.title("Komplexität")
plt.xlabel("Listenlänge")
plt.ylabel("Zeit in s")
plt.legend(loc="upper left")
plt.minorticks_on()
plt.show()