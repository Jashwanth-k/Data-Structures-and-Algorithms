
class BinaryTreeNode:

    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def printTreeDetailed(root):
    if root is None:
        return

    print(root.data,end=':')
    if root.left is not None:
        print('L',root.left.data,end=',')
    if root.right is not None:
        print('R',root.right.data,end='')
    print()

    printTreeDetailed(root.left)
    printTreeDetailed(root.right)

def inputTree():

    rootdata = int(input())
    if rootdata == -1:
        return None

    root = BinaryTreeNode(rootdata)
    rootleft = inputTree()
    rootright = inputTree()

    root.left = rootleft
    root.right = rootright
    return root

root = inputTree()
printTreeDetailed(root)