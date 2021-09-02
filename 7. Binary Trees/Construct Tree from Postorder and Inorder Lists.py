
import queue
q = queue.Queue()

class BinaryTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def printTree(root):

    if root is None:
        return

    q.put(root)

    while q.empty() is False:
        currNode = q.get()
        print(currNode.data,end=':')

        if currNode.left is not None:
            print('L',currNode.left.data,end=',')
            q.put(currNode.left)
        else:
            print('L'+'-1',end=',')

        if currNode.right is not None:
            print('R',currNode.right.data,end='')
            q.put(currNode.right)
            print()
        else:
            print('R'+'-1',end='')
            print()

def createTreefromPostInor(postorder,inorder):

#here -1 is the last index of postorder
    if len(postorder) == 0:
        return None

    rootdata = postorder[-1]
    root = BinaryTreeNode(rootdata)

    rootindex = -1
    for i in range(len(inorder)):
        if inorder[i] == root.data:
            rootindex = i
            break
    if rootindex == -1:
        return None

    leftinorder = inorder[:rootindex]
    rightinorder = inorder[rootindex+1:]

    lengthLI = len(leftinorder)

    leftpostorder = postorder[:lengthLI]
    rightpostorder = postorder[lengthLI:-1]

    leftchild = createTreefromPostInor(leftpostorder,leftinorder)
    rightchild = createTreefromPostInor(rightpostorder,rightinorder)

    root.left = leftchild
    root.right = rightchild
    return root

print('enter postorder:')
postorder = [ele for ele in input().split()]
print('enter inorder:')
inorder = [ele for ele in input().split()]

root = createTreefromPostInor(postorder,inorder)
printTree(root)


