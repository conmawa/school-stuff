## stack #ä#

class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            print("Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            print("Stack is empty")

    def size(self):
        return len(self.stack)
    
    def print_stack(self):
        if not self.is_empty():
            print("Stack elements:")
            for item in reversed(self.stack):
                print(item)
        else:
            print("Stack is empty")


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

stack.print_stack()

stack.pop()
stack.print_stack()