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
            currentNode = self.head
            while currentNode.next != None:
                currentNode = currentNode.next
            currentNode.next = newNode
        self.length += 1

    def insertAtGivenPosition(self, position, data):
        if position > self.length or position < 0:
            return None
        else:
            if position == 1:
                self.insertAtBeggining(data)
            elif position == self.length:
                self.insertAtEnd(data)
            else:
                newNode = Node(data)
                count = 1
                currentNode = self.head
                while count < position-1:
                    count += 1
                    currentNode = currentNode.next
                newNode.next = currentNode.next
                currentNode.next = newNode
                self.length += 1

    def deleteFromBeginning(self):
        if self.length != 0:
            self.head =  self.head.next
            self.length -= 1

    def deleteFromEnd(self):
        if self.length != 0:
            currentNode = self.head
            auxiliaryNode = self.head
            while currentNode.next != None:
                auxiliaryNode = currentNode
                currentNode = currentNode.next
            auxiliaryNode.next = None
            self.length -= 1

    def deleteFromGivenPosition(self, position):
        count = 1
        currentNode = self.head
        auxiliaryNode = self.head
        if position > self.length or position < 0:
            return None
        else:
            if position == 1:
                self.deleteFromBeginning()
            elif position == self.length:
                self.deleteFromEnd()
            else:
                while currentNode.next != None or count < position-1:
                    if count==position:
                        auxiliaryNode.next=currentNode.next
                        self.length -= 1
                        return
                    else:
                        auxiliaryNode=currentNode
                        currentNode=currentNode.next
                    count += 1

    def deleteAllFromGivenData(self, data):
        currentNode = self.head
        auxiliaryNode = self.head

        while currentNode.next != None:
            if self.head.data == data:
                self.head = currentNode.next
                self.length -= 1
            elif currentNode.data == data:
                auxiliaryNode.next = currentNode.next
                currentNode = auxiliaryNode
                self.length -= 1
            auxiliaryNode = currentNode
            currentNode = currentNode.next
        if currentNode.data == data:
            auxiliaryNode.next = currentNode.next
            self.length -= 1 

    def print(self):
        h = self.head
        while(h):
            print(f'{h.data} ->', end=' ')
            h=h.next
        print('\n')

list = LinkedList()

list.insertAtBeggining(1)
list.insertAtBeggining(2)
list.insertAtBeggining(2)
list.insertAtBeggining(3)
list.insertAtBeggining(3)
list.insertAtBeggining(3)
list.print()
list.insertAtEnd(1)
list.print()
list.insertAtGivenPosition(1, 5)
list.print()
list.insertAtGivenPosition(5, 6)
list.print()
list.insertAtGivenPosition(4, 7)
list.print()
list.deleteFromBeginning()
list.print()
list.deleteFromEnd()
list.print()
list.deleteFromGivenPosition(2)
list.print()
list.deleteFromGivenData(1)
list.print()
list.deleteAllFromGivenData(1)
list.print()
