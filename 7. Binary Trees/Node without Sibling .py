
class BinaryTreeNode:

    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def printTree(root):
    if root is None:
        return

    print(root.data,end=':')
    if root.left is not None:
        print('L',root.left.data,end=',')
    if root.right is not None:
        print('R',root.right.data,end='')
    print()

    printTree(root.left)
    printTree(root.right)

def Treeinput():

    rootdata = int(input())

    if rootdata == -1:
        return

    root = BinaryTreeNode(rootdata)
    root.left = Treeinput()
    root.right = Treeinput()

    return root

root = Treeinput()
printTree(root)
print()

def NodeWithout_siblings(root):

#A node is without siblings when a root as only one children
    if root is None:
        return

    elif root.left != None and root.right == None:
        print(root.left.data,end=' ')

    elif root.right != None and root.left == None:
        print(root.right.data,end=' ')


    NodeWithout_siblings(root.left)
    NodeWithout_siblings(root.right)

NodeWithout_siblings(root)

