
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
    q.put('null')

    while q.empty() is False:
        curr = q.get()

        if q.empty():
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


def takeinputLevelwise(l):

    if len(l) == 0:
        return

    rootdata = l[0]
    del l[0]
    if rootdata == -1:
        return None
    root = BinaryTreeNode(rootdata)
    q.put(root)

    while not q.empty():
        curr = q.get()

        currleft = l[0]
        del l[0]
        currright = l[0]
        del l[0]

        if currleft != -1:
            curr.left = BinaryTreeNode(currleft)
            q.put(curr.left)
        if currright != -1:
            curr.right = BinaryTreeNode(currright)
            q.put(curr.right)

    return root

inputlist = [int(ele) for ele in input().split()]
root = takeinputLevelwise(inputlist)
printTreelevelOrder(root)

