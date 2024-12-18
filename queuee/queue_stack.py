def reverseQueueUsingStack(queue, stack):

    while not queue.isEmpty():
        stack.push(queue.deQueue())

    while not stack.isEmpty():
        queue.enQueue(stack.pop())







