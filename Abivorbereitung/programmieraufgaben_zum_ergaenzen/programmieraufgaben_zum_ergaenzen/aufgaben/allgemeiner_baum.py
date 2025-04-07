# Allgemeiner Baum: Schul-Lehrplan
# --------------------------------
# Dieser Baum stellt eine Schulstruktur dar.
# - Die Wurzel ist die Schule selbst.
# - Jedes Fach hat mehrere Themenbereiche.
# - Jeder Themenbereich kann weitere Unterthemen haben.

# Aufgabe: Implementiere die fehlende Logik für `breadth_first_traversal()`!
# Die Funktion soll alle Fächer und Themen in der Reihenfolge der Hierarchie ausgeben.

class Node:
    def __init__(self, name):
        self.name = name
        self.children = []

class SchoolCurriculum:
    def __init__(self, school_name):
        self.root = Node(school_name)

    def insert(self, parent_name, child_name):
        """Fügt ein Fach oder Thema unter einem bestehenden Element hinzu."""
        parent_node = self.search(parent_name)
        if parent_node:
            parent_node.children.append(Node(child_name))
        else:
            print(f"'{parent_name}' nicht gefunden! '{child_name}' nicht eingefügt.")

    def search(self, name):
        """Sucht nach einem Fach oder Thema im Lehrplan."""
        queue = [self.root]

        while queue:
            current = queue.pop(0)
            if current.name == name:
                return current
            queue.extend(current.children)

        return None

    def breadth_first_traversal(self, current = None):
        """Breitensuche: Gibt die gesamte Lehrplanstruktur aus."""
        queue = []
        if current is None:
            queue.append(self.root)
        
        while queue:
            current = queue.pop(0)
            print(current.name, end=" ")
            queue.extend(current.children)
            
        # TODO: Implementiere hier die Breitensuche!
        # - Erstelle eine Warteschlange mit dem Wurzelknoten.
        # - Solange die Schlange nicht leer ist:
        #     - Entferne das erste Element
        #     - Gib seinen Namen aus
        #     - Füge alle Kinder dieses Knotens zur Schlange hinzu
        

# Test: Aufbau eines Schul-Lehrplans
schule = SchoolCurriculum("Gymnasium")

schule.insert("Gymnasium", "Mathematik")
schule.insert("Gymnasium", "Informatik")
schule.insert("Mathematik", "Algebra")
schule.insert("Mathematik", "Geometrie")
schule.insert("Informatik", "Programmieren")
schule.insert("Informatik", "Datenbanken")
schule.insert("Algebra", "Lineare Gleichungen")
schule.insert("Geometrie", "Dreiecke")
schule.insert("Programmieren", "Python Grundlagen")
schule.insert("Datenbanken", "SQL Abfragen")

print("Schul-Lehrplan (Breitensuche):")
schule.breadth_first_traversal()  # Erwartete Ausgabe: Gymnasium Mathematik Informatik Algebra Geometrie Programmieren Datenbanken Lineare Gleichungen Dreiecke Python Grundlagen SQL Abfragen

print()
print("Suche nach 'Programmieren':", schule.search("Programmieren") is not None)  # Erwartete Ausgabe: True
print("Suche nach 'Physik':", schule.search("Physik") is not None)  # Erwartete Ausgabe: False


