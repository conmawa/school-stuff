# Binärer Suchbaum (Binary Search Tree, BST)
# ------------------------------------------
# Ein binärer Suchbaum speichert Werte in einer Baumstruktur.
# - Linke Kinder sind kleiner als das Eltern-Element.
# - Rechte Kinder sind größer als das Eltern-Element.

# Aufgabe: Implementiere die fehlende Logik für `pre_order_traversal()`!
# Die Funktion soll die Werte in Einfügereihenfolge ausgeben (Wurzel, Links, Rechts).

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None  # Wurzel des Baumes (Startpunkt)

    def insert(self, value):
        """Fügt einen neuen Wert in den Baum ein."""
        if self.root is None:
            self.root = Node(value)
        else:
            current = self.root
            while True:
                if value < current.value:
                    if current.left is None:
                        current.left = Node(value)
                        break
                    else:
                        current = current.left
                else:
                    if current.right is None:
                        current.right = Node(value)
                        break
                    else:
                        current = current.right

    def search(self, value):
        """Sucht nach einem Wert im Baum."""
        current = self.root
        while current is not None:
            if current.value == value:
                return True  # Wert gefunden
            elif value < current.value:
                current = current.left  # Suche links weiter
            else:
                current = current.right  # Suche rechts weiter
        return False  # Wert nicht gefunden

    def in_order_traversal(self):
        """In-Order-Traversierung: Gibt die Werte sortiert aus (L, W, R)."""
        def traverse(node):
            if node is not None:
                traverse(node.left)
                print(node.value, end=" ")
                traverse(node.right)
        traverse(self.root)
        print()

    def pre_order_traversal(self, current=None):
        """Pre-Order-Traversierung: Gibt die Werte in Einfügereihenfolge aus (W, L, R)."""
        if current is None:
            current = self.root
        print(current.value, end=" ")
        if current.left is not None:
            self.pre_order_traversal(current.left)
        if current.right is not None:
            self.pre_order_traversal(current.right)
        # TODO: Implementiere hier die Pre-Order-Traversierung!
        # - Gib den Wert des aktuellen Knotens aus
        # - Gehe rekursiv nach links
        # - Gehe rekursiv nach rechts
        

baum = BinarySearchTree()
baum.insert(50)
baum.insert(30)
baum.insert(70)
baum.insert(20)
baum.insert(40)
baum.insert(60)
baum.insert(80)

print("In-Order Traversierung (sortierte Reihenfolge):")
baum.in_order_traversal()  # Erwartete Ausgabe: 20 30 40 50 60 70 80

print("Pre-Order Traversierung (Einfügereihenfolge):")
baum.pre_order_traversal()  # Erwartete Ausgabe: 50 30 20 40 70 60 80

print("Suche nach 40:", baum.search(40))  # Erwartete Ausgabe: True
print("Suche nach 25:", baum.search(25))  # Erwartete Ausgabe: False
