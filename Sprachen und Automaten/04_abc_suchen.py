## suchen ##
import random

def add():
    string = "abc"
    with open("H:\\abc_woerter.txt", "a") as files:
        for i in range(4):
            files.write(random.choice(string))
        files.write("\n")

for i in range(500):
    add()
    
with open("H:\\abc_woerter.txt", "r") as file:
    for element in file:
        if "aaa" in element:
            print(element)
        else:
            pass
    
