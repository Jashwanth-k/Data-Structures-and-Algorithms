
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

def Greaterthan_x(root,x,count=0):

    if root is None:
        return count

    rootleft = Greaterthan_x(root.left,x,count)
    rootright = Greaterthan_x(root.right,x,count)

    if root.data > x:
        count += 1

    return count + rootleft + rootright

x = int(input('enter x:'))
print('Nodes greater than x are:',Greaterthan_x(root,x))


