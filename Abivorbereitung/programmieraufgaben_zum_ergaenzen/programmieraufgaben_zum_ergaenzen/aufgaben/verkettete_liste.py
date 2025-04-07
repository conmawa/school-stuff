# Verkettete Liste (Linked List)
# ------------------------------
# Eine verkettete Liste besteht aus Knoten (Nodes), die miteinander verbunden sind.
# Jeder Knoten speichert einen Wert und eine Referenz auf den nächsten Knoten.

# Aufgabe: Implementiere die fehlende Logik für `pop()`!
# Die Methode soll das letzte Element der Liste entfernen und den Wert zurückgeben.

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

    def pop(self, current=None):
        """Entfernt das letzte Element der Liste."""
        if current is None:
            current = self.kopf
        if current.next is None:
            self.kopf = None
            return
        while current.next.next:
            current = current.next
        current.next = None
        # TODO: Implementiere hier die Pop-Logik!
        # Falls die Liste leer ist:
        #     - Rückgabe: None (weil nichts entfernt werden kann)
        #
        # Falls nur ein Element vorhanden ist:
        #     - Speichere den Wert
        #     - Setze den Kopf auf None
        #     - Rückgabe: gespeicherter Wert
        #
        # Falls mehrere Elemente vorhanden sind:
        #     - Gehe bis zum vorletzten Element
        #     - Speichere den Wert des letzten Knotens
        #     - Entferne das letzte Element (setze next auf None)
        #     - Rückgabe: gespeicherter Wert

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

liste.pop()
liste.display()  # Erwartete Ausgabe: 10 -> 20 -> None

liste.pop()
liste.display()  # Erwartete Ausgabe: 10 -> 20 -> None
