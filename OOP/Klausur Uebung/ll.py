
class Node:
    def __init__(self, data, nextNode = None):
        self.data = data
        self.nextNode = nextNode

class LinkedList:
    def __init__(self):
        self.head = None
    
    def add_first(self, data):
        self.head = Node(data, self.head)
    
    def add_end(self, data):
        current = self.head
        
        while current.nextNode:
            current = current.nextNode
        
        current.nextNode = Node(data)
    
    def print(self):
        current = self.head
        
        while current:
            print(current.data)
            current = current.nextNode
        
ll = LinkedList()

ll.add_first(3)
ll.add_end(333)
ll.add_first(88)
ll.print()