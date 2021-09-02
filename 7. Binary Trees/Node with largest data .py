
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

def largestdata(root):

    if root is None:
        return -1  #here we can return -infinity as least value

    leftlargest = largestdata(root.left)
    rightlargest = largestdata(root.right)

    return max(root.data,leftlargest,rightlargest)

print('largest Node in Bt is:',largestdata(root))