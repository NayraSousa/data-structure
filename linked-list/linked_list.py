from node import Node

class LinkedList:
    def __init__(self):
        self.length = 0
        self.head = None

    def insertAtBeggining(self, data):
        newNode = Node(data)
        if self.length == 0:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        self.length += 1

    def insertAtEnd(self, data):
        newNode = Node(data)
        if self.length == 0:
            self.head = newNode
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = newNode
        self.length += 1

    def insertAtGivenPosition(self, position, data):
        if position > self.length or position < 0:
            return None
        else:
            if position == 0:
                self.insertAtBeggining(data)
            elif position == self.length:
                self.insertAtEnd(data)
            else:
                newNode = Node(data)
                count = 1
                current = self.head
                while count < position-1:
                    count += 1
                    current = current.next
                newNode.next = current.next
                current.next = newNode
                self.length += 1

    def deleteFromBeginning(self):
        if self.length != 0:
            self.head =  self.head.next
            self.length -= 1

    def print(self):
        h = self.head
        while(h):
            print(f'{h.data} ->', end=' ')
            h=h.next
        print('\n')

list = LinkedList()
list.insertAtBeggining(10)
list.insertAtBeggining(10)
list.insertAtBeggining(1460)
list.print()
list.insertAtEnd(18)
list.print()
list.insertAtGivenPosition(0, 3)
list.print()
list.insertAtGivenPosition(5, 17)
list.print()
list.insertAtGivenPosition(4, 88)
list.print()
list.deleteFromBeginning()
list.print()