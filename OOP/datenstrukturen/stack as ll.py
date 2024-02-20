## stack using a linked list ##
# last in firt out #

class Node:
    def __init__(self, data, nextNode = None):
        self.data = data
        self.nextNode = nextNode
        
class Stack:
    def __init__(self, head = None):
        self.head = head
        
    def add_element(self, data):
        if self.head:
            node = self.head
            while node.nextNode != None:
                node = node.nextNode
            node.nextNode = Node(data)
        else:
            self.head = Node(data, self.head)
            
    def delete(self):
        if not self.head:
            print("stack is empty")
            return
            
        if not self.head.nextNode:
            self.head = None
            print("last element was deleted, stack is now empty")
            return
        
        current = self.head
        while current.nextNode.nextNode:
            current = current.nextNode
        current.nextNode = None
        print("element was deleted")
        
            
    def print_stack(self):
        current = self.head
        while current:
            print(current.data)
            current = current.nextNode
            
    def search_number(self, data):
        current = self.head
        was_found = False
        
        while current:
            if current.data == data:
                was_found = True
                break
            else:
                current = current.nextNode

        if was_found:
            print(data, "was found")
        else:
            print(data, "was not found")
        
    
stack = Stack()
for i in range(5):
    stack.add_element(i)

print("normal stack.")
stack.print_stack()
stack.delete()


print("deleted stack:") 
stack.print_stack()

stack.search_number(10)