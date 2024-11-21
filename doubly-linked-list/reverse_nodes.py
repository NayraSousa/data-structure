class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertAtBeginning(self, data):
        newNode = Node(data)
        if self.head==None:
            self.head = self.tail = newNode
        else:
            newNode.previous = None
            newNode.next = self.head
            self.head.previous = newNode
            self.head = newNode


    def reverseNodes(self):
        currentNode = self.head
        previousNode = None
        while currentNode != None:
            nextNode = currentNode.next
            currentNode.next = previousNode
            previousNode = currentNode
            currentNode = nextNode
        self.head = previousNode

    def printNext(self):
        h = self.head
        while(h):
            print(f'{h.data} ->', end=' ')
            h=h.next
        print('\n')

    def printPrevious(self):
        h = self.head
        while(h):
            print(f'{h.data} ->', end=' ')
            h=h.previous
        print('\n')

list = LinkedList()
list.insertAtBeginning(4)
list.insertAtBeginning(5)
list.insertAtBeginning(7)
list.insertAtBeginning(8)
list.insertAtBeginning(1)
list.insertAtBeginning(67)
list.printNext()
list.reverseNodes()
list.printNext()