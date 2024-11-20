from node import Node

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    def insertAtBeginning(self, data):
        newNode = Node(data)
        if self.head==None:
            self.head = self.tail = newNode
        else:
            newNode.previous = None
            newNode.next = self.head
            self.head.previous = newNode
            self.head = newNode
            self.length += 1
        
