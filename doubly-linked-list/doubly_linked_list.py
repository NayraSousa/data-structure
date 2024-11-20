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
            self.length += 1
        else:
            newNode.previous = None
            newNode.next = self.head
            self.head.previous = newNode
            self.head = newNode
            self.length += 1

    def insertAtEnd(self, data):
        if self.head==None:
            self.head = Node(data)
            self.length += 1
        else:
            currentNode = self.head
            while currentNode.next != None:
                currentNode = currentNode.next
            newNode = Node(data)
            currentNode.next = newNode
            newNode.previous = currentNode
            newNode.next = None
            self.length += 1

    def insertAtGivenPosition(self, position, data):
        if self.head==None or position==1:
            self.insertAtBeginning(data)
        elif position==self.length:
            self.insertAtEnd(data)
        else:
            currentNode = self.head
            count = 0
            while currentNode != None and count < position:
                currentNode = currentNode.next
                count += 1
            newNode = Node(data)
            newNode.next = currentNode.next
            newNode.previous = currentNode
            currentNode.next = newNode
            self.length += 1
            
    def print(self):
        h = self.head
        while(h):
            print(f'{h.data} <->', end=' ')
            h=h.next
        print('\n')

list = DoublyLinkedList()
list.insertAtBeginning(4)
list.insertAtBeginning(5)
list.print()
list.insertAtEnd(1)
list.insertAtEnd(1)
list.print()
list.insertAtBeginning(8)
list.print()
list.insertAtGivenPosition(5, 9)
list.print()
print(list.length)




