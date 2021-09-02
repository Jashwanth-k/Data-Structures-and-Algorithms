
import queue
q = queue.Queue()
#create Queue first itself

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
            print()
            q.put(currNode.right)
        else:
            print('R'+'-1',end='')
            print()

    return

def takelevelwiseInput():

    print('enter root')
    rootdata = int(input())
    if rootdata == -1:
        return None
    root = BinaryTreeNode(rootdata)
    q.put(root)

    while q.empty() is False:
        currNode = q.get()
        print('enter the left child of',currNode.data)
        currNodeleft = int(input())
        print('enter the right child of',currNode.data)
        currNoderight = int(input())

        if currNodeleft != -1:
            currNode.left = BinaryTreeNode(currNodeleft)
            q.put(currNode.left)

        if currNoderight != -1:
            currNode.right = BinaryTreeNode(currNoderight)
            q.put(currNode.right)

    return root

root = takelevelwiseInput()
printTreelevelwise(root)


