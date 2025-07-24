# Singly Linked List Implementation

# Arrray: [->5, {}10, {}15, {}20, {}25]

class Node:
    def __init__ (self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__ (self):
        self.head = None # Start of the linked list

# Add to front
    def insert_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

# Print the linked list
    def print_list(self):
        curr = self.head

        while curr:
            print(curr.data, end=" -> ")
            curr = curr.next
        print("None")



if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_front(5)
    ll.insert_front(10)
    ll.insert_front(15)
    ll.insert_front(20)

    ll.print_list()



# LIFO (Last In First Out) - Stack

# Doubly Linked List Implementation

class DNone:
    def __init__(self, data):
        self.data = data # Value stored in the node
        self.next = None # Pointers to the next nodes
        self.prev = None # Pointers to the previous nodes

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Add to front
    def insert_front(self, data):
        new_node = DNone(data)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node
        new_node.prev = None

    # Print the doubly linked list
    def print_list(self):
        curr = self.head
        while curr:
            print(curr.data, end=" <-> ")
            curr = curr.next
        print("None")

if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.insert_front(5)
    dll.insert_front(10)
    dll.insert_front(15)
    dll.insert_front(20)

    dll.print_list()