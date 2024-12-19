class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinSearchTree:
    def __init__(self):
        self.root = None

    def search(self, data, node=None):
        if node is None:
            return None
        if data == node.data:
            return node
        elif data < node.data:
            return self.search(data, node.left)
        else:
            return self.search(data, node.right)

    def insert(self, data, node=None):
        if node is None:
            return Node(data)
        if data < node.data:
            node.left = self.insert(data, node.left)
        elif data > node.data:
            node.right = self.insert(data, node.right)
        return node

    def remove(self, data, node=None):
        if node is None:
            return node
        if data < node.data:
            node.left = self.remove(data, node.left)
        elif data > node.data:
            node.right = self.remove(data, node.right)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            node.data = self.minimum(node.right).data
            node.right = self.remove(node.data, node.right)
        return node

    def minimum(self, node=None):
        current = node
        while current.left:
            current = current.left
        return current

    def inOrder(self, node=None):
        if node is None:
            return []
        return self.inOrder(node.left) + [node.data] + self.inOrder(node.right)


