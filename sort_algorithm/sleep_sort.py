from random import randint
import threading
from time import sleep

def sleep_and_print(element):
    sleep(element)
    print(element, end = '')
    
    
def sleep_sort(array):
    threads = []
    for element in array:
        thread = threading.Thread(target=sleep_and_print, args=(element,))
        threads.append(thread)
        thread.start()
        
    for thread in threads:
        thread.join()

lst = []
for i in range(10):
    lst.append(randint(0,10))
    
print(sleep_sort(lst))