## Graph ##
from random import randint
class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.insert(0, data)
    
    def dequeue(self):
        if self.queue:
            return self.queue.pop(0)
        else:
            raise IndexError("Die Queue ist leer, kein Element zum Dequeuen")
    
    def isEmpty(self):
        # Überprüfe, ob die Queue leer ist
        return len(self.queue) == 0


class Graph():
    def __init__(self, size):
        self.size = size
        self.graph = [[] for _ in range(size)]
    
    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def bfs(self, start):
        # Führt eine Breitensuche (BFS) vom Startknoten aus durch
        visited = [False] * self.size
        queue = Queue()
        queue.enqueue(start)
        visited[start] = True

        while not queue.isEmpty():
            # Entfernt den aktuellen Knoten aus der Queue und druckt ihn
            current = queue.dequeue()
            print(current, end=" ")

            # Gehe alle Nachbarn des aktuellen Knotens durch
            for neighbor in self.graph[current]:
                # Wenn der Nachbar noch nicht besucht wurde, füge ihn zur Queue hinzu
                if not visited[neighbor]:
                    queue.enqueue(neighbor)
                    visited[neighbor] = True
                    
    def find_path(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        for neighbor in self.graph[start]:
            if neighbor not in path:
                new_path = self.find_path(neighbor, end, path)
                if new_path:
                    return new_path
        return None


gp = Graph(10)

for i in range(10):
    gp.add_edge(randint(0,9), randint(0,9))

#gp.bfs(0)

start_node = 1
end_node = 8
path = gp.find_path(start_node, end_node)

if path:
    print(f"Pfad von {start_node} nach {end_node}: {path}")
else:
    print(f"Kein Pfad von {start_node} nach {end_node} gefunden.")