
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

    if root is None:
        return 0

    return 1 + max(height(root.left),height(root.right))

def isBalanced(root):
#T.C is (nh)

    if root is None:
        return True

    lh = height(root.left)
    rh = height(root.right)

#if differences of heights are > [1] we should return False since unBalanced
    if lh - rh > 1 or rh - lh > 1:
        return False

    rootleft = isBalanced(root.left)
    rootright = isBalanced(root.right)

#here we should use 'and' instead of 'or' bcz both must be True inorder to be balanced
    if rootleft and rootright:
        return True
    else:
        return False

#print(isBalanced(root))

def isRootBalanced(root):
#T.C is O(n)

    if root is None:
        return True,0

    isleftBalanced,lh = isRootBalanced(root.left)
    isrightBalanced,rh = isRootBalanced(root.right)

    height = 1 + max(lh,rh)

    if lh - rh > 1 or rh - lh > 1:
        return False,height

    if isleftBalanced and isrightBalanced:
        return True,height
    else:
        return False,height

def isBalanced2(root):

#this function is created for only returning 'True' or 'False' excluding the height
    RootBalanced,h = isRootBalanced(root)
    return RootBalanced

print(isBalanced2(root))
