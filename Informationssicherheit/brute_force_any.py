## Brute-Force ##

from random import randint
import matplotlib.pyplot as plt 
from timeit import default_timer

def brute_force(word):
    global count, counts, times
    start = default_timer()
    target_array = list(word)
    string_array = [""] * len(target_array)
    count = 0
    counts = []
    times = []
    
    while string_array != target_array:
        for i in range(len(target_array)):
            for j in range(256):
                if string_array[i] != target_array[i]:
                    string_array[i] = chr(j)
                    count += 1
                end = default_timer()
                time = end - start
                counts.append(count)
                times.append(time)
                print("".join(string_array))
            
    
    



text = "Hallihallo, wie gehts wie stehts? Heute ist ja so ein tolles Wetter *hust *hust"
brute_force(text)
print(f"Total guesses: {count}")

plt.plot(counts, times, label="text")
plt.grid()
plt.title("Brute-Force")
plt.xlabel("Guesses")
plt.ylabel("time in s")
plt.legend(loc="upper left")
plt.minorticks_on()
plt.show()
