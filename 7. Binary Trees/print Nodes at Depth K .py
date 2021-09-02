
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

#for printing nodes at depth k by decrementing 'k'
def printdepth_K(root,k):

    if root is None:
        return

    if k == 0:
        print(root.data,end=' ')
        return

    printdepth_K(root.left,k-1)
    printdepth_K(root.right,k-1)

#for printing nodes at depth k by maintaining count as 'd'
def printdepth_atk(root,k,d=0):

    if root is None:
        return

    if k == d:
        print(root.data,end=' ')
        return

    printdepth_atk(root.left,k,d+1)
    printdepth_atk(root.right,k,d+1)

k = int(input('enter k value:'))
printdepth_atk(root,k)

