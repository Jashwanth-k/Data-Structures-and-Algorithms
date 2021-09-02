
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


def takeinputLevelwise():

    #print('enter root data')
    rootdata = int(input())
    if rootdata == -1:
        return None
    root = BinaryTreeNode(rootdata)
    q.put(root)

    while not q.empty():
        curr = q.get()
        #print('enter the left child of',curr.data)
        currleft = int(input())
        #print('enter the right child of',curr.data)
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


def print_k1tok2(root,k1,k2):

    if root is None:
        return

    if root.data > k2:
        print_k1tok2(root.left,k1,k2)

    elif root.data < k1:
        print_k1tok2(root.right,k1,k2)

#the root is middle of k1 and k2 so we will print root.data and call recursion on both sides
    else:
        print(root.data)
        print_k1tok2(root.left,k1,k2)
        print_k1tok2(root.right,k1,k2)

print()
print_k1tok2(root,6,10)
