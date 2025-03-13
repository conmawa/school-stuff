import csv
def auslesen():
    kaufdaten = []
    with open('meier_01.csv', newline = '') as file:
        lines = csv.reader(file, delimiter = ' ', quotechar = ';')
        for rwo in lines:
            print(
    
auslesen()