from insert_tree import buildRandomTree

def maxValueRecursive(root):
    if root is None:
        return 0

    maxValueLeft = maxValueRecursive(root.left)
    maxValueRight = maxValueRecursive(root.right)

    return max(maxValueLeft, maxValueRight, root.data)

tree, root = buildRandomTree(45, 10)
tree.inOrder(root)
print()
print(maxValueRecursive(root))
