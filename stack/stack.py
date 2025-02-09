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
        return self.array[self.top-1]
    
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

    def invertVector(self, vector):

        for element in vector:
            self.push(element)

        for count in range(len(vector)):
            vector[count] = self.pop()
        return vector

    
