
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

def print_inorder(root):

#for inorder in TREE we need to print as : leftside,root,rightside
    if root is None:
        return

    print_inorder(root.left)

    print(root.data,end=' ')

    print_inorder(root.right)


def ReplaceNodes_depth(root,count=0):

#if root is not None root.data will be replaced by depth of TREE i.e count
    if root is None:
        return

    root.data = count

    ReplaceNodes_depth(root.left,count+1)
    ReplaceNodes_depth(root.right,count+1)

ReplaceNodes_depth(root)
print_inorder(root)

