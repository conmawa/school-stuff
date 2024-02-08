## binary tree ##

from random import randint

class Node():
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right
        
class Binary_Tree():
    def __init__(self):
        self.root = None
    
    def add_root(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            raise Exception("You already got one root! Just one root is required!")
    
    def add_child(self, data, node = None):
        if node is None:
            node = self.root
        
        if node is None:
            self.add_root(data)
        else:
            if data < node.data:
                if node.left is None:
                    node.left = Node(data)
                else:
                    self.add_child(data, node.left)
                    
            elif data > node.data:
                if node.right is None:
                    node.right = Node(data)
                else:
                    self.add_child(data, node.right)
                    
            elif data == node.data:
                if node.left is None:
                    node.left = Node(data)
                else:
                    self.add_child(data, node.left)
        
    def print_pre_order(self, node = None):
        if node is None:
            node = self.root
        
        if node:
            print(node.data)
            
            if node.left:
                self.print_pre_order(node.left)
                
            if node.right:
                self.print_pre_order(node.right)
        
    def print_in_order(self, node = None):
        if node is None:
            node = self.root
        
        if node:
            if node.left:
                self.print_in_order(node.left)
            
            print(node.data)
            
            if node.right:
                self.print_in_order(node.right)
        
    def print_post_order(self, node = None):
        if node is None:
            node = self.root
        
        if node:
            if node.left:
                self.print_post_order(node.left)
                
            if node.right:
                self.print_post_order(node.right)
                
            print(node.data)
    
    def search_number(self, data, node = None):
        if node is None:
            node = self.root
        
        if data > node.data:
            if node.right:
                self.search_number(data, node.right)
            else:
                print(data, "was not found!")
                
        elif data < node.data:
            if node.left:
                self.search_number(data, node.left)
            else:
                print(data, "was not found!")
                
        elif data == node.data:
            print(data, "was found!")
            
        else:
            print(data, "was not found!")
      
      
    def delete(self, data, node = None, parent = None):
        if node is None:
            node = self.root
        
        if data < node.data and node.left:
            node.left = self.delete(data, node.left, node)
        
        elif data > node.data and node.right:
            node.right = self.delete(data, node.right, node)
                
        elif data == node.data:
            # Fall mit keinem / einem Kind #
            if node.left is None:
                print(data, "was succesfully deleted")
                return node.right
            
            if node.right is None:
                print(data, "was succesfully deleted")
                return node.left
            
            # Fall für zwei Kinder #
            temp = self.min_node(node.right)
            node.data = temp.data
            node.right = self.delete(temp.data, node.right, node)
            
            print(data, "was succesfully deleted")
           
        else:
            print(data, "was not found!")
            
        return node
    
    def min_node(self, node = None):
        if node is None:
            node = self.root
        
        while node.left:
            node = node.left
        
        return node
       
       
        
bt = Binary_Tree()

# für random Baum #
# bt.add_root(randint(0,100))
# for i in range(10):
#     bt.add_child(randint(0,100))
    
# für eigenen Baum #
bt.add_root(8)
bt.add_child(3)
bt.add_child(1)
bt.add_child(6)
bt.add_child(7)
bt.add_child(4)
bt.add_child(10)
bt.add_child(14)
bt.add_child(13)

# für random Baum #
# for i in range (1, 100+1):
#     bt.search_number(i)
    
# für eigenen Baum #
# search_number = int(input("number to search for:"))
# bt.search_number(search_number)


# print("pre-order:")
# bt.print_pre_order()
# print("-----------")
# print("in-order:")
# bt.print_in_order()
# print("-----------")
# print("post-order:")
# bt.print_post_order()

# funktioniert nur für 10, warum?? Auch wenn die Zahl gar nicht erst existiert
bt.delete(1)
# print("in-order:")
# bt.print_in_order()