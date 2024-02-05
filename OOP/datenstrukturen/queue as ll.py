## queue using a linked list ##
# first in first out #

class Node:
    def __init__(self, data, nextNode = None):
        self.data = data
        self.nextNode = nextNode
        
class Queue:
    def __init__(self, head = None):
        self.head = head
    
    def add_element(self, data):
        self.head = Node(data, self.head)
        
    def delete(self):
        if self.head:
            self.head = self.head.nextNode
            print("element was deleted")
        else:
            print("queue is empty")
        
    def print_queue(self):
        current = self.head
        while current:
            print(current.data)
            current = current.nextNode

queue = Queue()
for i in range(1):
    queue.add_element(i)
queue.print_queue()
queue.delete()
queue.delete()
queue.print_queue()