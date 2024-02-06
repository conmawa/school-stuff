## Aufgabe von ChatGPT ##

class Rechner:
    def addition(self, zahl1, zahl2):
        print(f"{zahl1} + {zahl2} = {zahl1 + zahl2}")
    
    def subtraktion(self, zahl1, zahl2):
        print(f"{zahl1} - {zahl2} = {zahl1 - zahl2}")
    
    def multiplikation(self, zahl1, zahl2):
        print(f"{zahl1} x {zahl2} = {zahl1 * zahl2}")
    
    def division(self, zahl1, zahl2):
        print(f"{zahl1} : {zahl2} = {zahl1 / zahl2}")
    
    def ist_primzahl(self, number):
        if number <= 1:
            return False
        for i in range(2, int(number**0.5) + 1):
            if number % i == 0:
                return False
        return True
    

rechner = Rechner()

rechner.addition(10,12)
rechner.subtraktion(10,12)
rechner.multiplikation(10,12)
rechner.division(10,12)
num = 23
if rechner.ist_primzahl(num):
    print(f"{num} ist eine Primzahl")
else:
    print(f"{num} ist keine Primzahl")