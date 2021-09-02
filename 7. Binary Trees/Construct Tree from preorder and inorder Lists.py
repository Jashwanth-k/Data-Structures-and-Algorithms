
import queue
q = queue.Queue()

class BinaryTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def printTreelevelwise(root):

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

def createTreeformInPre(preorder,inorder):

# if preorder is empty simply return None
    if len(preorder) == 0:
        return None

    rootdata = preorder[0]
    root = BinaryTreeNode(rootdata)

    rootindex = -1
    for i in range(len(inorder)):
        if inorder[i] == root.data:
            rootindex = i
            break
    if rootindex == -1: #if unable to find index
        return None

    leftinorder = inorder[:rootindex]
    rightinorder = inorder[rootindex+1:]

    lengthLI = len(leftinorder)

    leftpreorder = preorder[1:lengthLI+1]
    rightpreorder = preorder[lengthLI+1:]

    leftchild = createTreeformInPre(leftpreorder,leftinorder)
    rightchild = createTreeformInPre(rightpreorder,rightinorder)

    root.left = leftchild
    root.right = rightchild
    return root

print('enter preorder:')
preorder = [ele for ele in input().split()]
print('enter inorder:')
inorder = [ele for ele in input().split()]
root = createTreeformInPre(preorder,inorder)
printTreelevelwise(root)
