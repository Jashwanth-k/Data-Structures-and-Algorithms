
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
            print()
            q.put(currNode.right)
        else:
            print('R'+'-1',end='')
            print()

    return

def takeinputLevelwise():

    print('enter root')
    rootdata = int(input())
    if rootdata == -1:
        return None
    root = BinaryTreeNode(rootdata)
    q.put(root)

    while not q.empty():

        currNode = q.get()
        print('enter the left child of',currNode.data)
        leftchild = int(input())
        print('enter the right child of',currNode.data)
        rightchild = int(input())

        if leftchild != -1:
            currNode.left = BinaryTreeNode(leftchild)
            q.put(currNode.left)

        if rightchild != -1:
            currNode.right = BinaryTreeNode(rightchild)
            q.put(currNode.right)

    return root

root = takeinputLevelwise()
#printTree(root)

def find_MaxandMin(root):

#here float('inf') is infinity 
    if root is None:
        return float('inf'),float('-inf')

    leftmin,leftmax = find_MaxandMin(root.left)
    rightmin,rightmax = find_MaxandMin(root.right)

    return min(root.data,leftmin,rightmin),max(root.data,leftmax,rightmax)

print(find_MaxandMin(root))


