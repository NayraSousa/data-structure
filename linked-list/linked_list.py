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