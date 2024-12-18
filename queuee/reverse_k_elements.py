from queue import Queue

def reverseKElements(queue, k):

    auxiliary = []

    for _ in range(k):
        auxiliary.append((queue.get()))

    remaining_queue = queue.qsize()

    while auxiliary:
        queue.put(auxiliary.pop())

    for _ in range(remaining_queue):
        queue.put(queue.get())

fila = Queue()

elementos = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
for elem in elementos:
    fila.put(elem)
reverseKElements(fila, 3)

while not fila.empty():
    print(fila.get(), end=" ")
