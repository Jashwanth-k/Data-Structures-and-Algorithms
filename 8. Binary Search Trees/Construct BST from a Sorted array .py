
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
    q.put('Null')

    while q.empty() is False:
        curr = q.get()

        if q.empty():
            return

        if curr == 'Null':
            print()
            q.put('Null')

        else:
            print(curr.data,end=' ')

            if curr.left != None:
                q.put(curr.left)

            if curr.right != None:
                q.put(curr.right)

def constructBSTfromarray(list1):
    if len(list1) == 0:
        return

#Here when length of list is '1' we can just create a root and return rather than calling recursion
    if len(list1) == 1:
        mid = list1[0]
        root = BinaryTreeNode(mid)
        return root

    mid = len(list1)//2
    root = BinaryTreeNode(list1[mid])

    leftlist = list1[:mid]
    rightlist = list1[mid+1:]

    leftTree = constructBSTfromarray(leftlist)
    rightTree = constructBSTfromarray(rightlist)

    root.left = leftTree
    root.right = rightTree

    return root

list1 = [ele for ele in input().split()]
root = constructBSTfromarray(list1)
printTreelevelOrder(root)
