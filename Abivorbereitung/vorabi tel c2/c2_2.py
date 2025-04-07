from csv import *

def count_elements(products, all_products):
    anzahl = {}
    for element in products:
        anzahl[element] = all_products.count(element)
    max_count = {}
    max_count[element] = max(anzahl[element] for element in products)
    return max_count
    
def main():
    with open('vorlage_c2-2.csv', newline = '') as csvfile:
        spamreader = reader(csvfile, delimiter = ',')
        snacks_counter = 0
        drinks_counter = 0
        all_products = []
        products = []
        for row in spamreader:
            if 'Produktcode' != row[0]:
                if 'S' in row[0]:
                    snacks_counter += 1
                elif 'G' in row[0]:
                    drinks_counter += 1
                all_products.append(row[0])
                if row[0] not in products:
                    products.append(row[0])
                    
    most = count_elements(products, all_products)
                
    with open('auswertung_verkauf_automat.csv', 'w', newline = '') as newfile:
        spamwriter = writer(newfile, delimiter=',')
        spamwriter.writerow(['Anzahl Produkte', snacks_counter + drinks_counter])
        spamwriter.writerow(['Anzahl Snacks', snacks_counter])
        spamwriter.writerow(['Anzahl Getraenke', drinks_counter])
        spamwriter.writerow(['Meistverkauftes Produkt', most])
    
    print(all_products)
    print('Anzahl der verkauften Produkte:', snacks_counter + drinks_counter)
    print('Anzahl der verkauften Snacks:', snacks_counter)
    print('Anzahl der verkauften Getränke:', drinks_counter)
    print('Meist verkauftes Produkt:', most)
            
main()