import random

class Stack:
    def __init__(self, capacity=1):
        self.top = 0
        self.capacity=capacity
        self.array = [None]*capacity
    
    def push(self, data):
        if self.capacity==self.top:
            print("Stack Overflow")
            return
        self.array[self.top]=data
        self.top+=1

    def pop(self):
        if self.top==-1:
            print("Stack Underflow")
            return
        auxiliary = self.array[self.top-1]
        self.top-=1
        return auxiliary
    
    def peek(self):
        if self.top==-1:
            print("Stack Overflow")
            return
        return self.array[self.top]
    
    def size(self):
        return self.top
    
    def isEmpty(self):
        return self.top == 0
    
    def isFull(self):
        return self.capacity==self.top+1
    
    def removeElementsRecursively(self, stack):
        if stack.isEmpty():
            return
        print(stack.pop())
        self.removeElementsRecursively(stack)
        
stack = Stack(6)
for count in range(6):
    stack.push(random.randint(1, 21))

print(stack.removeElementsRecursively(stack))
    
