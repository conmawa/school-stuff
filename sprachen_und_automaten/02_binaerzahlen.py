## Binärzahlen in .txt ##

from random import randint

with open("H:\\binaerzahlen1.txt", "w") as file:
        file.write("")
        
for i in range(100):
    zahl = ""
    for j in range(8):
        zahl = zahl + str(randint(0,1))
    with open("H:\\binaerzahlen1.txt", "a") as file:
        file.write(f"\n{zahl}")

with open("H:\\binaerzahlen1.txt", "r") as file:
    ergebnis = file.read()

print(ergebnis)