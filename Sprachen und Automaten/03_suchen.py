## geradde Binärzahlen ##

import matplotlib.pyplot as plt

gerade = 0
ungerade = 0

with open("H:\\gerade_binaerzahlen.txt", "a") as file_neu:
    with open("H:\\binaerzahlen.txt", "r") as file:
        for element in file:
            string = element.strip()
            if string.endswith("0"):
                gerade += 1
                file_neu.write(string)
            else:
                ungerade += 1

with open("H:\\gerade_binaerzahlen.txt", "r") as file_neu:
    print(file_neu.read())
    
print(f"Es gibt {ungerade} ungerade und {gerade} gerade Binärzahlen")

anzahl = [gerade, ungerade]
x = ["gerade Binärzahlen", "ungerade Binärzahlen"]

plt.bar(x, anzahl, linewidth=0.5)
plt.title("Suchen in Datein")
plt.ylabel("Anzahl")
plt.minorticks_on()
plt.show()