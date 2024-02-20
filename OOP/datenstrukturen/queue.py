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
        
    def is_empty(self):
        return len(self.queue) == 0
        
    def print_queue(self):
        if not self.is_empty():
            print("Queue elements:")
            for item in reversed(self.queue):
                print(item)
        else:
            print("Queue is empty")
    
    def search_number(self, data):
        was_found = False
        for i in range(len(self.queue)):
            if self.queue[i] == data:
                was_found = True
        
        if was_found:
            print(data, "was found")
        else:
            print(data, "was not found")

queue = Queue()

queue.enqueue(39)
queue.enqueue(1)
queue.print_queue()

# queue.dequeue()
# queue.dequeue()
# queue.dequeue()


queue.search_number(1)
