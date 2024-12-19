from insert_tree import buildRandomTree
from collections import deque

def maxValueRecursive(root):
    if root is None:
        return 0

    maxValueLeft = maxValueRecursive(root.left)
    maxValueRight = maxValueRecursive(root.right)

    return max(maxValueLeft, maxValueRight, root.data)

def maxValue(root):
    if root is None:
        return None
    queue = deque([root])
    maxValue = root.data

    while queue:
        node = queue.popleft()
        if node.data > maxValue:
            maxValue = node.data
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return maxValue

