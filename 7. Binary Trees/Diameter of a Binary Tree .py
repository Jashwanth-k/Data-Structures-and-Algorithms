
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
        return None

    root = BinaryTreeNode(rootdata)
    root.left = Treeinput()
    root.right = Treeinput()
    return root

root = Treeinput()
printTree(root)
print()

def height(root):
#T.C is O(nh)

    if root is None:
        return 0

    return 1 + max(height(root.left),height(root.right))

def diameter(root):

    if root is None:
        return 0

#for the case if deepest Nodes present on left and right sides
    option1 = height(root.left) + height(root.right)
#if deepest Node present only on left side
    option2 = diameter(root.left)
#id deepest Node present only on right side
    option3 = diameter(root.right)

    return 1 + max(option1,option2,option3)

#print('The diameter of root is:',diameter(root))


def DiameterWithHeight(root):
#T.C is O(n)

    if root is None:
        diameter = 0
        height = 0
        return diameter,height

    option2,leftheight = DiameterWithHeight(root.left)
    option3,rightheight = DiameterWithHeight(root.right)
    option1 = leftheight + rightheight

    height = 1 + max(leftheight,rightheight)

    return 1 + max(option1,option2,option3),height

print('The diameter of tree is:',DiameterWithHeight(root))

