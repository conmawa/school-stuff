# Verkettete Liste (Linked List)
# ------------------------------
# Eine verkettete Liste besteht aus Knoten (Nodes), die miteinander verbunden sind.
# Jeder Knoten speichert einen Wert und eine Referenz auf den nächsten Knoten.
#
# - Die Klasse `Node` stellt einen einzelnen Knoten mit `wert` und `next` dar.
# - Die Klasse `LinkedList` verwaltet die gesamte Liste.
#   - `append(wert)`: Fügt ein Element am Ende hinzu.
#   - `pop()`: Entfernt das letzte Element.
#   - `display()`: Gibt alle Elemente der Liste aus.

class Node:
    def __init__(self, wert):
        self.wert = wert  # Speichert den Wert des Knotens
        self.next = None  # Verweist auf den nächsten Knoten (standardmäßig None)

class LinkedList:
    def __init__(self):
        self.kopf = None  # Der erste Knoten der Liste (initial leer)

    def append(self, wert):
        """Fügt ein neues Element am Ende der Liste hinzu."""
        neuer_knoten = Node(wert)  # Erstelle einen neuen Knoten

        if self.kopf is None:  # Falls die Liste leer ist, setze den Kopfknoten
            self.kopf = neuer_knoten
        else:
            aktueller = self.kopf
            while aktueller.next:  # Gehe bis zum letzten Knoten
                aktueller = aktueller.next
            aktueller.next = neuer_knoten  # Hänge den neuen Knoten an das Ende

    def pop(self):
        """Entfernt das letzte Element der Liste."""
        if self.kopf is None:  # Falls die Liste leer ist, gibt es nichts zu entfernen
            return None

        if self.kopf.next is None:  # Falls nur ein Element vorhanden ist
            wert = self.kopf.wert
            self.kopf = None  # Liste ist danach leer
            return wert

        aktueller = self.kopf
        while aktueller.next.next:  # Gehe bis zum vorletzten Element
            aktueller = aktueller.next

        wert = aktueller.next.wert  # Wert des letzten Elements speichern
        aktueller.next = None  # Letztes Element entfernen
        return wert

    def display(self):
        """Gibt alle Elemente der Liste aus."""
        aktueller = self.kopf
        while aktueller:
            print(aktueller.wert, end=" -> ")
            aktueller = aktueller.next
        print("None")  # Zeigt das Ende der Liste an

# Test
liste = LinkedList()
liste.append(10)
liste.append(20)
liste.append(30)
liste.display()  # Erwartete Ausgabe: 10 -> 20 -> 30 -> None

liste.pop()
liste.display()  # Erwartete Ausgabe: 10 -> 20 -> None
