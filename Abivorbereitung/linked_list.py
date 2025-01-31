
class Node:
    def __init__(self, data, nextNode = None):
        self.data = data
        self.nextNode = nextNode
        
class LinkedList:
    def __init__(self):
        self.head = None
    
    def is_empty(self):
        return self.head is None
    
    def insert_at_start(self, data):
        self.head = Node(data, self.head)
        
    def insert_at_end(self, data):
        if self.is_empty():
            self.head = Node(data, self.head)
        else:
            current = self.head
            while current.nextNode:
                current = current.nextNode
            current.nextNode = Node(data)
            
    def delete_at_start(self):
        if self.is_empty():
            print('Linked List is empty')
        else:
            self.head = self.head.nextNode
    
    def delete_at_end(self):
        if self.is_empty():
            print('Linked List is empty')
        else:
            current = self.head
            while current.nextNode.nextNode:
                current = current.nextNode
            current.nextNode = None
    
    def delete_in_middle(self, data):
        if self.is_empty():
            print('Linked List is empty')
        else:
            current = self.head
            if current.data == data:
                self.delete_at_start()
                return
            
            while current:
                if current.nextNode.data == data:
                    current.nextNode = current.nextNode.nextNode
                    return
                current = current.nextNode
    
    def show(self):
        if self.is_empty():
            print('Linked List is empty')
        else:
            current = self.head
            while current:
                print(current.data)
                current = current.nextNode
    
    def search_number(self, data):
        if self.is_empty():
            print('Linked List is empty')
        else:
            current = self.head
            while current:
                if current.data == data:
                    print(f'{data} was found')
                    return
                current = current.nextNode
            print(f'{data} was not found')
        
ll = LinkedList()
for i in range(10):
    ll.insert_at_end(i)
print('new')
ll.show()

ll.delete_at_start()
print('at start')
ll.show()

ll.delete_at_end()
print('at end')
ll.show()

ll.delete_in_middle(5)
print('in middle')
ll.show()

ll.search_number(0)
