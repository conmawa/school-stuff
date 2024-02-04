## Queue ##

class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.insert(0, data)
    
    def dequeue(self):
        if self.queue:
            return self.queue.pop(0)
        else:
            raise IndexError("Queue is empty. Cannot dequeue an empty queue.")

queue1 = Queue()
print(queue1.queue)
queue1.enqueue(39)
queue1.enqueue(1)
print(queue1.queue)

queue1.dequeue()
queue1.dequeue()
queue1.dequeue()
print(queue1.queue)
