
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

def sumofNodes(root):
#here when root is None we should return sum = 0. instead of None becz we cant add None + None
    if root is None:
        return 0

    leftdata = sumofNodes(root.left)
    rightdata = sumofNodes(root.right)

    return root.data + leftdata + rightdata

def Treeinput():

    rootdata = int(input())
    if rootdata == -1:
        return None

    root = BinaryTreeNode(rootdata)
    root.left = Treeinput()
    root.right = Treeinput()
    return root

root = Treeinput()
printTree(root)
print('sum of Nodes are:',sumofNodes(root))