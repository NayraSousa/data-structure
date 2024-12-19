def checkItem(root, item):
    if root is None:
        return False
    if root.data == item:
        return True
    return checkItem(root.left, item) or checkItem(root.right, item)

