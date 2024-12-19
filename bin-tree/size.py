from insert_tree import buildRandomTree
from collections import deque

def sizeOfTreeRecursive(root):
    if root is None:
        return 0

    return 1 + sizeOfTreeRecursive(root.left) + sizeOfTreeRecursive(root.right)

def sizeOfTree(root):
    if root is None:
        return 0

    queue = deque([root])
    size = 0
    while queue:
        node = queue.popleft()
        size+=1

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return size

