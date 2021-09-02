
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
        print('L',root.left.data,end=',')
    if root.right is not None:
        print('R',root.right.data,end='')
    print()

    printTree(root.left)
    printTree(root.right)

def height(root,h=0):

    if root is None:
        return h

    rootleft = height(root.left,h)
    rootright = height(root.right,h)

    if rootleft > rootright:
        return 1 + rootleft
    return 1 + rootright

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

def printlevel_wise(root,level):
    if root is None:
        return

    if level == 1:
        print(root.data,end=' ')

    else:
        if level > 1:
            printlevel_wise(root.left,level-1)
            printlevel_wise(root.right,level-1)

def inorder(root):
    h = height(root)
    for i in range(1,h+1):
        printlevel_wise(root,i)

def Mirror_Tree(root):

#we should swap the roots left and right simultaneously
    if root is None:
        return None

    if root is not None:
        root.left,root.right = root.right,root.left

    Mirror_Tree(root.left)
    Mirror_Tree(root.right)
    return root

root = Mirror_Tree(root)
inorder(root)


