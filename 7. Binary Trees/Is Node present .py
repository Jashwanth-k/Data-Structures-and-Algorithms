
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

def isNode_present(root,x):

    if root is None:
        return False

    elif root.data == x:
        return True

    rootleft = isNode_present(root.left,x)
    rootright = isNode_present(root.right,x)

    if rootleft is True or rootright is True:
        return True

    return False

x = int(input('enter x value:'))
print(isNode_present(root,x))

