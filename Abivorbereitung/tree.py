class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, value):
        node = TreeNode(value)
        self.children.append(node)
        return node

    def pre_order(self):
        print(self.value)
        for element in self.children:
            element.pre_order()

    def in_order(self):
        if len(self.children) > 0:
            self.children[0].in_order()
        print(self.value)
        
        for child in self.children[1:]:
            child.in_order()
        
    def post_order(self):
        for element in self.children:
            element.post_order()
        print(self.value)
        
    def breiten_suche(self):
        queue = []
        queue.append(self)
        
        while len(queue) > 0:
            current = queue.pop(0)
            print(current.value)
            
            for child in current.children:
                queue.append(child)
            

anna = TreeNode('Anna')
maria = anna.add_child('Maria')
paul = anna.add_child('Paul')
lisa = maria.add_child('Lisa')
tom = maria.add_child('Tom')
sara = paul.add_child('Sara')


print('pre order:')
anna.pre_order()
print('')
print('in order:')
anna.in_order()
print('')
print('post order:')
anna.post_order()
print('')
print('Breiten Suche:')
anna.breiten_suche()