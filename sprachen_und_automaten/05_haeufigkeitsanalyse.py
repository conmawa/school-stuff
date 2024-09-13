## Häufigkeitsanalyse ##

import matplotlib.pyplot as plt
import io

with io.open("\text.txt", "r", encoding = "utf-8") as file:
    buchstaben_in_string = []
    buchstaben = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    anzahl = []
    for element in file:
        element = element.lower()
        element = element.replace("ä", "ae")
        element = element.replace("ö", "oe")
        element = element.replace("ß", "ss")
        
        for letter in element:
            if letter.islower():
                buchstaben_in_string.append(letter)
            else:
                buchstaben_in_string.append(letter.lower())
            
    for element in buchstaben:
        zahl = buchstaben_in_string.count(element)
        anzahl.append(zahl)
    
plt.bar(buchstaben, anzahl, linewidth=0.5)
plt.title("Häufigkeitsanalyse")
plt.ylabel("Anzahl")
plt.minorticks_on()
plt.show()