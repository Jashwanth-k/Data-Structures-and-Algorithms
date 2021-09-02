import queue
q = queue.Queue()

class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children = list()

def printTree(root):
    if root is None:
        return

    print(root.data,end=':')
    for child in root.children:
        print(child.data,end=',')
    print()

    for child in root.children:
        printTree(child)

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
        numChildren = int(input())

        for i in range(numChildren):
            print('enter',currNode.data,'next child:')
            childNodes = TreeNode(int(input()))
            currNode.children.append(childNodes)
            q.put(childNodes)

    return root

root = takeinputLevelWise()
printTree(root)




