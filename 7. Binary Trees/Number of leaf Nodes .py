
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

def numof_leafnodes(root,number):

    if root is None:
        return number

    rootleft = numof_leafnodes(root.left,number)
    rootright = numof_leafnodes(root.right,number)

    if root.right is None and root.left is None:
        number += 1

    return number + rootleft + rootright


print('No of leaf Nodes are:',numof_leafnodes(root,0))



