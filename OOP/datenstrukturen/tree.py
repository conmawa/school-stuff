## Tree ##

class Node:
    def __init__(self, data):
        self.data = data
        self.left = []
        self.right = []
        
class Tree:
    def __init__(self):
        self.root = None
    
    def add_root(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            raise Exception("You already got one root! Just one root is required!")
    
    def add_child(self, data, position, parent):
        current = self.root
        
        if parent == current.data:
            if position == "left":
                current.left.append(Node(data))
            elif position == "right":
                current.right.append(Node(data))
            else:
                raise Exception("Wrong position argument! Please use either 'left' or 'right'.")
        else:
            pass
        
        
tree = Tree()
tree.add_root(10)
print(tree.root.data)

tree.add_child(364, "left", 10)
print(tree.root.right[0].data)