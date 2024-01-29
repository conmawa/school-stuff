## Queue ##

class Queue():
    def __init__(self):
        self.liste = []

    def enqueue(self, data):
        self.liste.insert(0, data)
    
    def dequeue(self):
        pass

queue1 = Queue()
print(queue1.liste)
queue1.enqueue(39)
queue1.enqueue(1)
print(queue1.liste)
