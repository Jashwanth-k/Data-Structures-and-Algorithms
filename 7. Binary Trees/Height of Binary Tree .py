
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

def Heightof_Tree(root,height=0):

    if root is None:
        return height

    leftheight = Heightof_Tree(root.left,height)
    rightheight = Heightof_Tree(root.right,height)

    if leftheight > rightheight:
        return 1 + leftheight

    return 1 + rightheight

print('Height of the Tree is:',Heightof_Tree(root))