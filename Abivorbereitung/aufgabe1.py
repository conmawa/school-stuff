
def auslesen():
    with open('meier_01.csv', mode = 'r') as file:
        lines = file.readlines()
        print(lines)
    
auslesen()