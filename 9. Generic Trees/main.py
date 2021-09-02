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
    q.put(None)

    while not q.empty():
        currNode = q.get()

        if q.empty():
            return

        if currNode == None:
            print()
            q.put(None)
        else:
            print(currNode.data,end=' ')
            for child in currNode.children:
                q.put(child)

    return

def takeinputLevelWise(inputlist):
    if len(inputlist) == 0:
        return

    if inputlist[0] == -1:
        return
    rootdata = inputlist[0]
    del inputlist[0]

    root = TreeNode(rootdata)
    q.put(root)

    while not(q.empty()):
        currNode = q.get()
        numChildren = inputlist[0]
        del inputlist[0]

        for i in range(numChildren):
            childNodes = TreeNode(inputlist[0])
            del inputlist[0]
            currNode.children.append(childNodes)
            q.put(childNodes)

    return root


inputlist = [int(ele) for ele in input().split()]
root = takeinputLevelWise(inputlist)
printTreeLevelWise(root)
print()
print()

def Helper(root,depth):

    root.data = depth
    for child in root.children:
        Helper(child,depth+1)

def Replace_depth(root,depth=0):
#take default depth as zero

    if root is None:
        return

    root.data = depth

    for child in root.children:
        Helper(child,depth+1)

    return root

root = Replace_depth(root)
printTreeLevelWise(root)

