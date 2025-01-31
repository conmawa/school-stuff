## queue using a linked list ##
# first in first out #

class Node:
    def __init__(self, data, nextNode = None):
        self.data = data
        self.nextNode = nextNode
        
class Queue:
    def __init__(self, head = None):
        self.head = head
    
    def is_empty(self):
        if self.head is None:
            return True
    
    def add_element(self, data):
        if self.is_empty():
            self.head = Node(data, self.head)
        else:
            node = self.head
            while node.nextNode != None:
                node = node.nextNode
            node.nextNode = Node(data)
        
    def delete(self):
        if self.is_empty:
            print("queue is empty")
        else:
            self.head = self.head.nextNode
            print("element was deleted")
        
    def print_queue(self):
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

queue = Queue()
for i in range(10):
    queue.add_element(i)
queue.print_queue()
queue.delete()
queue.delete()
queue.print_queue()

queue.search_number(10)