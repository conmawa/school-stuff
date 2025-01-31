class Node:
    def __init__(self, value, nextNode = None):
        self.value = value
        self.nextNode = nextNode

class Queue:
    def __init__(self):
        self.head = None
    
    def enqueue_v1(self, value):
        self.head = Node(value, self.head)

    def enqueue_v2(self, value):
        current = self.head
        if not current:
            self.head = Node(value, self.head)
        else:
            while current.nextNode:
                current = current.nextNode
            current.nextNode = Node(value)
            
    def dequeue_v1(self):
        current = self.head
        if not current:
            raise Exception('Queue is empty')
        else:
            while current.nextNode.nextNode:
                current = current.nextNode
            print(f'Element {current.nextNode.value} wurde gelöscht')
            current.nextNode = None

    def dequeue_v2(self):
        print(f'Element {self.head.value} wurde gelöscht')
        self.head = self.head.nextNode

    def wartezeit_bestimmen(self, average):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.nextNode
        return count * average
    
    def print(self):
        current = self.head
        while current:
            print(current.value)
            current = current.nextNode

q_v1 = Queue()
q_v2 = Queue()
for i in range(1,5):
    q_v1.enqueue_v1(i)
    
print('first')
q_v1.print()
print('Wartezeit: ', q_v1.wartezeit_bestimmen(5), 'min')

# q_v1.dequeue_v1()
# print('first')
# q_v1.print()

for i in range(1,5):
    q_v2.enqueue_v2(i)
    
print('second')
q_v2.print()
print('Wartezeit: ', q_v2.wartezeit_bestimmen(20), 'min')

# q_v2.dequeue_v2()
# print('second')
# q_v2.print()