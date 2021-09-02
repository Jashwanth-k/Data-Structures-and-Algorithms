
import queue
q = queue.Queue()

class BinaryTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def printTreelevelOrder(root):
#null will be used as reference to indicate the completion of level

    if root is None:
        return

    q.put(root)
    q.put('null')

    while q.empty() is False:
        curr = q.get()

        if q.empty(): #if queue is empty just come out of loop else this will be infinity loop
            break

        if curr == 'null':
            print()
            q.put('null')
        else:
            print(curr.data,end=' ')

            if curr.left != None:
                q.put(curr.left)

            if curr.right != None:
                q.put(curr.right)


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
printTreelevelOrder(root)

