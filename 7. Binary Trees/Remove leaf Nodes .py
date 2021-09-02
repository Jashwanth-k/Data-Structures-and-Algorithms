
class BinaryTree:

    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def printTree(root):

    if root is None:
        return

    print(root.data,end=':')
    if root.left is not None:
        print(root.left.data,end=',')
    if root.right is not None:
        print(root.right.data,end='')
    print()

    printTree(root.left)
    printTree(root.right)

def inputTree():

    rootdata = int(input())
    if rootdata == -1:
        return

    root = BinaryTree(rootdata)
    root.left = inputTree()
    root.right = inputTree()

    return root

root = inputTree()
printTree(root)
print()


def remove_leaves(root):

    if root is None:
        return None

    if root.left is None and root.right is None:
        return None

#we need to update roots left and right. If it returns None
    root.left = remove_leaves(root.left)
    root.right = remove_leaves(root.right)
    return root

root = remove_leaves(root)
printTree(root)


