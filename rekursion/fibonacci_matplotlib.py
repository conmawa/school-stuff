from matplotlib.pyplot import *
from timeit import timeit

def fib(n):
    if n == 1 or n == 0:
        return n
    else:
        return fib(n-1) + fib(n-2)
    
def find_komblexity():
    x = []
    y = []
    for i in range(0, 40):
        print(i)
        x.append(i)
        y.append(timeit(lambda: fib(i), number=1))
    
    plot(x, y, marker="o", label="Fibonacci Folge")
    grid()
    title("Komplexität")
    xlabel("n")
    ylabel("Zeit in s")
    legend(loc="upper left")
    minorticks_on()
    show()



find_komblexity()
