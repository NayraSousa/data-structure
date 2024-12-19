from insert_tree import buildRandomTree

def heightOfTree(root):
    if root is None:
        return -1

    heightLeft = heightOfTree(root.left)
    heightRight = heightOfTree(root.right)

    return 1 + max(heightRight, heightLeft)
