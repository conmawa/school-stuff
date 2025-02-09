class Node:
    def __init__(self, data):
        self.data = data
        self.neighbours = []

class Graph:
    def __init__(self):
        self.nodes = []

    def add_node(self, data):
        node = Node(data)
        self.nodes.append(node)
        return node

    def add_edge(self, data, neighbour_data):
        node = self.find_node(data)
        neighbour = self.find_node(neighbour_data)
        if node and neighbour:
            node.neighbours.append(neighbour)

    def find_node(self, data):
        for node in self.nodes:
            if node.data == data:
                return node
        return None

    def show(self):
        for node in self.nodes:
            print(node.data, end=' -> ')
            for neighbour in node.neighbours:
                print(neighbour.data, end=' ')
            print()

    def show_neighbours(self, data):
        node = self.find_node(data)
        if node:
            print(f"Neighbours of {data}: ", end='')
            for neighbour in node.neighbours:
                print(neighbour.data, end=' ')
            print()
        else:
            print(f"Node with data {data} not found.")

# Example usage
graph = Graph()
graph.add_node(1)
graph.add_node(2)
graph.add_node(3)
graph.add_node(4)
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 3)
graph.add_edge(3, 4)
graph.show()
graph.show_neighbours(1)
graph.show_neighbours(2)
graph.show_neighbours(3)