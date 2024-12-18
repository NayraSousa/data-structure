class Queue:
    def __init__(self, limit=5):
        self.queue = [None]*limit
        self.limit = limit
        self.front = 0
        self.rear = 0
        self.size = 0
    
    def isEmpty(self):
        return self.size <= 0

    def enQueue(self, item):
        if self.size == self.limit:
            return "Array is full"
        else:
            self.queue[self.rear] = item
            self.rear = (self.rear+1)%self.limit
            self.size += 1

    def deQueue(self):
        if self.size == 0:
            return
        else:
            item =self.queue[self.front]
            self.front = (self.front+1)%self.limit
            self.size -= 1
            return item

    def queueRear(self):
        if self.size>0:
            return self.queue[self.rear-1]
        else:
            raise IndexError

    def queueFront(self):
        if self.size>0:
            return self.queue[self.front]
        else:
            raise IndexError
