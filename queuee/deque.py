class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.previous = None

class Deque:
    def __init__(self):
        self.front = None
        self.rear = None

    def addFront(self, value):
        newNode = Node(value)
        if not self.front:
            self.front = self.rear = newNode
        else:
            newNode.next = self.front
            self.front.previous = newNode
            self.front = newNode

    def addRear(self, value):
        newNode = Node(value)
        if not self.rear:
            self.front = self.rear = newNode
        else:
            self.rear.next = newNode
            newNode.previous = self.rear
            self.rear = newNode

    def removeFront(self):
        if not self.front:
            return None
        removedValue = self.front.value
        if self.front == self.rear:
            self.front == self.rear == None
        else:
            self.front = self.front.next
            self.front.previous = None
        return removedValue

    def removeRear(self):
        if not self.rear:
            return None
        removedValue = self.rear.value
        if self.front == self.rear:
            self.front == self.rear == None
        else:
            self.rear = self.rear.previous
            self.rear.next = None
        return removedValue
