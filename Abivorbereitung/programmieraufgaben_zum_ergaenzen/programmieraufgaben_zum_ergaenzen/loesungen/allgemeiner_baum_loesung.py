# Allgemeiner Baum: Schul-Lehrplan
# --------------------------------
# Dieser Baum stellt eine Schulstruktur dar.
# - Die Wurzel ist die Schule selbst.
# - Jedes Fach hat mehrere Themenbereiche.
# - Jeder Themenbereich kann weitere Unterthemen haben.
#
# Wichtige Operationen:
# - `insert(parent_name, child_name)`: Fügt ein Fach oder Thema unter einem bestehenden Knoten hinzu.
# - `search(name)`: Sucht nach einem Fach oder Thema.
# - `breadth_first_traversal()`: Gibt die gesamte Lehrplanstruktur Level für Level aus.

class Node:
    def __init__(self, name):
        self.name = name  # Name des Fachs oder Themas
        self.children = []  # Liste der Unterthemen

class SchoolCurriculum:
    def __init__(self, school_name):
        self.root = Node(school_name)  # Die Schule als Wurzel

    def insert(self, parent_name, child_name):
        """Fügt ein Fach oder Thema unter einem bestehenden Element hinzu."""
        parent_node = self.search(parent_name)  # Suche nach der übergeordneten Struktur
        if parent_node:
            parent_node.children.append(Node(child_name))  # Füge das Fach oder Thema hinzu
        else:
            print(f"'{parent_name}' nicht gefunden! '{child_name}' nicht eingefügt.")

    def search(self, name):
        """Sucht nach einem Fach oder Thema im Lehrplan."""
        queue = [self.root]  # Warteschlange für die Breitensuche

        while queue:
            current = queue.pop(0)  # Nächstes Element entfernen
            if current.name == name:
                return current  # Gefunden!
            queue.extend(current.children)  # Alle Unterthemen hinzufügen

        return None  # Falls nicht gefunden

    def breadth_first_traversal(self):
        """Breitensuche: Gibt die gesamte Lehrplanstruktur Level für Level aus."""
        queue = [self.root]  # Warteschlange für die Breitensuche

        while queue:
            current = queue.pop(0)  # Nächstes Element aus der Schlange nehmen
            print(current.name, end=" ")  # Name des aktuellen Knotens ausgeben
            queue.extend(current.children)  # Alle Unterthemen hinzufügen

        print()  # Neue Zeile für bessere Darstellung

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

print("Suche nach 'Programmieren':", schule.search("Programmieren") is not None)  # Erwartete Ausgabe: True
print("Suche nach 'Physik':", schule.search("Physik") is not None)  # Erwartete Ausgabe: False
