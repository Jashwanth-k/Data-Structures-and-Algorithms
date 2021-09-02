
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

import queue
def takelevelwiseInput():

    q = queue.Queue()
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
printTree(root)


