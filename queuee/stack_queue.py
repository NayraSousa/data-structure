def reverseStackUsingQueue(stack, queue):

    while not stack.isEmpty():
        queue.enQueue(stack.pop())

    while not queue.isEmpty():
        stack.push(queue.deQueue())

