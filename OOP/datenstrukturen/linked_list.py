## Linked Lists ##

class Node:
    def __init__(self, data, nextNode = None):
        # wenn nutzer keine nextNode angibt => None
        # sonst wird es überschrieben
        self.data = data
        self.nextNode = nextNode
        
class LinkedList:
    def __init__(self):
        self.head = None
        # Nutzer muss beim initialisieren keine Werte angeben,
        # head wird immer None gesetzt.
        
    def insert_at_start(self, data):
        self.head = Node(data, self.head)
        
    def print_linked_list(self):
        # current ist Speichervaribale, damit self.head nicht verändert wird
        current = self.head
        while current:
            print(current.data, "-->")
            current = current.nextNode
            
    def print_linked_list_beaut(self):
        current = self.head
        ll_str = ""
        while current:
            ll_str = ll_str + current.data + "-->"
            current = current.nextNode
        print(ll_str)
        
    def insert_at_end(self, data):
        if self.head:
            node = self.head
            while node.nextNode != None:
                node = node.nextNode
            node.nextNode = Node(data)
        
    def search_number(self, data):
        current = self.head
        was_found = False
        
        while current:
            if current.data == data:
                was_found = True
                break
            else:
                current = current.nextNode

        if was_found:
            print(data, "was found")
        else:
            print(data, "was not found")
            
ll = LinkedList()
ll.insert_at_start("Eis")
ll.insert_at_end("Rum")
ll.insert_at_end("Cola")
ll.insert_at_end("Limette")
ll.insert_at_end("Minze")


ll.print_linked_list_beaut()

ll.search_number("Glas")