knotenliste = ['A', 'B', 'C', 'D']
adjazenzmatrix = [[0, 1, 0, 0], [0, 1, 1, 1], [1, 1, 0, 0], [0, 0, 0, 0]]

def existiertKnoten(knoten):
    for i in range(len(knotenliste)):
        if knotenliste[i] == knoten:
            print("True")
            break
    print("False")

existiertKnoten("B")