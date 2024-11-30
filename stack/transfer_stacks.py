from stack import Stack
import random

def transferStack(stackS, stackT):
    while stackS.isEmpty() != True:
        stackT.push(stackS.pop())

    return stackT

stackS = Stack(6)
stackT = Stack(6)
for count in range(6):
    stackS.push(random.randint(1, 21))
for count in range(6):
    print(transferStack(stackS, stackT).pop())

