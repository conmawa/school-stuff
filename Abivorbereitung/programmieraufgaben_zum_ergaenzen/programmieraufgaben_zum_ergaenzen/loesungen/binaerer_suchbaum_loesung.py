# Binärer Suchbaum (Binary Search Tree, BST)
# ------------------------------------------
# Ein binärer Suchbaum speichert Werte in einer Baumstruktur:
# - Linke Kinder sind kleiner als das Eltern-Element.
# - Rechte Kinder sind größer als das Eltern-Element.
#
# Wichtige Operationen:
# - `insert(value)`: Fügt einen neuen Wert in den Baum ein.
# - `search(value)`: Sucht nach einem Wert im Baum.
# - `in_order_traversal()`: Gibt die Werte sortiert aus (L, W, R).
# - `pre_order_traversal()`: Gibt die Werte in der Reihenfolge ihrer Einfügung aus (W, L, R).

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
            self.root = Node(value)  # Falls der Baum leer ist, setze die Wurzel
        else:
            current = self.root
            while True:  # Solange nicht eingefügt wurde
                if value < current.value:  # Falls der Wert kleiner ist, gehe nach links
                    if current.left is None:
                        current.left = Node(value)
                        break
                    else:
                        current = current.left
                else:  # Falls der Wert größer oder gleich ist, gehe nach rechts
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
                traverse(node.left)  # Gehe nach links
                print(node.value, end=" ")  # Gib den aktuellen Wert aus
                traverse(node.right)  # Gehe nach rechts
        traverse(self.root)
        print()  # Neue Zeile nach der Ausgabe

    def pre_order_traversal(self):
        """Pre-Order-Traversierung: Gibt die Werte in Einfügereihenfolge aus (W, L, R)."""
        def traverse(node):
            if node is not None:
                print(node.value, end=" ")  # Gib den aktuellen Wert aus
                traverse(node.left)  # Gehe nach links
                traverse(node.right)  # Gehe nach rechts
        traverse(self.root)
        print()  # Neue Zeile nach der Ausgabe

# Test
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
