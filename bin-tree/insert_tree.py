from bin_tree import Node, BinaryTree
import random

def buildRandomTree(seed, size):
    root = Node(seed)
    binTree = BinaryTree(root)
    i = 1

    while(i < size):
        p = q = root
        number = random.randint(0, size*40)
        while number != p.data and q != None:
            p=q
            if number<p.data:
                q = p.left
            else:
                q = p.right
        if number == p.data:
            continue
        elif number<p.data:
            p.setLeft(number)
        else:
            p.setRight(number)
        i+=1
    return binTree, root

