from csv import *


def count_elements(array):
    pass
    
def main():
    with open('vorlage_c2-2.csv', newline = '') as csvfile:
        spamreader = reader(csvfile, delimiter = ',')
        product_counter = 0
        snacks_counter = 0
        drinks_counter = 0
        array = []
        for row in spamreader:
            if 'Produktcode' != row[0]:
                product_counter += 1
                if 'S' in row[0]:
                    snacks_counter += 1
                elif 'G' in row[0]:
                    drinks_counter += 1
                array.append(row[0])
    
    with open('auswertung_verkauf_automat.csv', 'w', newline = '') as newfile:
        spamwriter = writer(newfile, delimiter=',')
        spamwriter.writerow(['Anzahl Produkte', product_counter])
        spamwriter.writerow(['Anzahl Snacks', snacks_counter])
        spamwriter.writerow(['Anzahl Getränke', drinks_counter])
    
    print(array)
    print('Anzahl der verkauften Produkte:', product_counter)
    print('Anzahl der verkauften Snacks:', snacks_counter)
    print('Anzahl der verkauften Getränke:', drinks_counter)
            
main()