x = 4

#rekursive Erstellung der Fakultät ## 0! = 1
def fak_r(n):
    if n == 0:
        return 1
    else:
        n = n * fak_r(n-1)
    return n

print(fak_r(x))

#iterative Erstellung der Fakultät
def fak_i(n):
    for i in range(1,n):
        n = n*i
    return n

print(fak_i(x))


#Fibonacci-Folge
def fi(n):
    if n == 0 or n == 1:
        return n
    else:
        return fi(n-1) + fi(n-2)
print(fi(25))

#Zinsrechnung

startkapital = 10000
jahres_zins = 5
jahre = 2

def zins(x, y, z):
    if z == 1:
        return 1
    else:
        z = (x*y)/100 * zins(x,y,z-1)
        return z
    
print(zins(startkapital, jahres_zins, jahre))