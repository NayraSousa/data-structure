class Node:
    def __init__(self, data=None, next=None, previous=None):
        self.data = data
        self.next = next
        self.previous = previous

    def __str__(self):
        return "Node[Data=%s]" % self.data

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def enQueue(self, data):
        if(self.size == 0):
            node = Node(data)
            self.front = node
            self.rear = node
            self.size += 1
        else:
            node = Node(data)
            self.rear.next = node
            node.previous = self.rear
            self.rear = node
            self.size += 1

    def deQueue(self):
        if self.size == 0:
            raise IndexError
        else:
            node = self.front.data
            self.front = self.front.next
            self.size -= 1
            return node

    def front(self):
        return self.front.data

    def rear(self):
        return self.rear.data