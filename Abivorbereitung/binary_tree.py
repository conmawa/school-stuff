class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
class BinaryTree:
    def __init__(self):
        self.root = None
        
    def insert(self, data, node = None):
        if node is None:
            node = self.root
            
        if node is None:
            self.root = Node(data)
        else:
            if data > node.data:
                if node.right:
                    self.insert(data, node.right)
                else:
                    node.right = Node(data)
                    
            elif data < node.data:
                if node.left:
                    self.insert(data, node.left)
                else:
                    node.left = Node(data)
                    
            elif data == node.data:
                if node.left:
                    self.insert(data, node.left)
                else:
                    node.left = Node(data)
    
    def in_order(self, node = None):
        if node is None:
            node = self.root
        
        if node:
            if node.left:
                self.in_order(node.left)
            print(node.data)
            if node.right:
                self.in_order(node.right)
        else:
            print('Error')
            
    def search_number(self, data):
        node = self.root
        while node:
            if data < node.data:
                node = node.left
            elif data > node.data:
                node = node.right
            else:
                print(data, 'was Found')
                break
        else:
            print(data, 'was not found')

bt = BinaryTree()
bt.insert(8)
bt.insert(3)
bt.insert(1)
bt.insert(6)
bt.insert(7)
bt.insert(4)
bt.insert(10)
bt.insert(14)
bt.insert(13)

bt.in_order()

bt.search_number(10)
bt.search_number(111)