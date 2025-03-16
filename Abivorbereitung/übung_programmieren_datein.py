from csv import reader


def open_file():
    with open('Abivorbereitung\datei.csv', 'r') as file:
        csv_reader = reader(file, delimiter = ';')
        return list(csv_reader)

def anzeigen():
    csv_reader = open_file()
    for row in csv_reader:
        if row[0] != 'Dateiname':
            print(f'Name: {row[0]}, Größe: {row[1]} MB')

def ordner_ansicht():
    csv_reader = open_file()
    for row in csv_reader:
        print(f'Name: {row[0]}')
        
def max_groesse():
    csv_reader = open_file()
    max_groesse = 0
    for row in csv_reader:
        if row[0] != 'Dateiname':
            if int(row[1]) > max_groesse:
                max_groesse = int(row[1])
    #print(f'Die größte Datei hat {max_groesse} MB')
    return max_groesse

def gesamt_groesse():
    csv_reader = open_file()
    gesamt_groesse = 0
    for row in csv_reader:
        if row[0] != 'Dateiname':
            gesamt_groesse += int(row[1])
    #print(f'Die gesamte Größe der Dateien beträgt {gesamt_groesse} MB')
    return gesamt_groesse

def abweichung(name):
    csv_reader = open_file()
    for row in csv_reader:
        if row[0] != 'Dateiname':
            if row[0] == name:
                abweichung =  max_groesse() - int(row[1])
                print(f'Die Datei {name} weicht um {abweichung} MB von der gesamten Größe ab.')

def ordner_zip():
    csv_reader = open_file()
    with open('Abivorbereitung\zip_ordner.csv', 'w') as file:
        for row in csv_reader:
            if row[0] != 'Dateiname':
                    file.write(f'{row[0]};{int(row[1])/2}\n')
        

anzeigen()
print('Maximal Größe: ', max_groesse())
print('Gesamte Größe: ', gesamt_groesse())
abweichung('Video1')
abweichung('Foto1')
ordner_zip()