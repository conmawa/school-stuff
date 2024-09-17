## files ##

with open("H:\\mein_satz.txt", "w") as file:
    ausgabe = file.write("Hallo")

with open("H:\\mein_satz.txt", "a") as file:
    ausgabe = file.write("\nWie gehts, wie stehts")

with open("H:\\mein_satz.txt", "r") as file:
    ausgabe = file.read()

print(ausgabe)