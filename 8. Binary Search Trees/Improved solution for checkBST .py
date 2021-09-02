
import queue
q = queue.Queue()

class BinaryTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def printTreelevelOrder(root):

    if root is None:
        return

    q.put(root)
    while not q.empty():
        curr = q.get()
        print(curr.data,end=':')

        if curr.left is not None:
            print('L',curr.left.data,end=',')
            q.put(curr.left)
        else:
            print('L'+'-1',end=',')

        if curr.right is not None:
            print('R',curr.right.data,end='')
            print()
            q.put(curr.right)
        else:
            print('R'+'-1',end='')
            print()

def takeinputLevelwise():

    print('enter root data')
    rootdata = int(input())
    if rootdata == -1:
        return None
    root = BinaryTreeNode(rootdata)
    q.put(root)

    while not q.empty():
        curr = q.get()
        print('enter the left child of',curr.data)
        currleft = int(input())
        print('enter the right child of',curr.data)
        currright = int(input())

        if currleft != -1:
            curr.left = BinaryTreeNode(currleft)
            q.put(curr.left)
        if currright != -1:
            curr.right = BinaryTreeNode(currright)
            q.put(curr.right)

    return root

root = takeinputLevelwise()
printTreelevelOrder(root)
print()

def isBST(root):

#here we need to find minimum,,maximum,isBST from one recursive call itself
    if root is None:
        return float('inf'),float('-inf'),True

    leftmin,leftmax,isleftBST = isBST(root.left)
    rightmin,rightmax,isrightBST = isBST(root.right)
    isTreeBST = True

    minimum = min(root.data,leftmin,rightmin)
    maximum = max(root.data,leftmax,rightmax)

    if root.data <= leftmax or root.data > rightmin:
        isTreeBST = False

    if not(isleftBST) or not(isrightBST):
        isTreeBST = False

    return minimum,maximum,isTreeBST

print(isBST(root))
