class Node:
    def __init__(self, value, nextNode = None):
        self.value = value
        self.nextNode = nextNode

class Stack:
    def __init__(self):
        self.head = None

    def add_element(self, value):
        self.head = Node(value, self.head)

    def delete_element(self):
        self.head = self.head.nextNode

    def klammer_pruefen(self, string):
        string = list(string)
        for element in string:
            if element == '(' or element == ')':
                self.add_element(element)
                
        current = self.head
        counter_one = counter_two = 0
        while current:
            if current.value == '(':
                counter_one += 1
            elif current.value == ')':
                counter_two += 1
            current = current.nextNode

        if counter_one == counter_two:
            print('Klammern richtig geschlossen')
        else:
            print('Klammern nicht richtig geschlossen')

s = Stack()
math_term1 = '(a+b) * (c-d)'
s.klammer_pruefen(math_term1)

math_term2 = '(((aa*2d)*34(g)d)'
s.klammer_pruefen(math_term2)