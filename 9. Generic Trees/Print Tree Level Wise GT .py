import queue
q = queue.Queue()

class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children = list()

def printTreeLevelWise(root):
    if root is None:
        return

    q.put(root)

    while not(q.empty()):
        currNode = q.get()
        print(currNode.data,end=':')

        for child in currNode.children:
            print(child.data,end=',')
            q.put(child)
        print()

    return

def takeinputLevelWise():

    print('Enter root data')
    rootdata = int(input())
    if rootdata == -1:
        return

    root = TreeNode(rootdata)
    q.put(root)

    while not(q.empty()):
        currNode = q.get()
        print('enter no of children for:',currNode.data)
        numchildren = int(input())

        for i in range(numchildren):
            print('enter',currNode.data,'next child:')
            childNodes = TreeNode(int(input()))
            currNode.children.append(childNodes)
            q.put(childNodes)

    return root

root = takeinputLevelWise()
printTreeLevelWise(root)



