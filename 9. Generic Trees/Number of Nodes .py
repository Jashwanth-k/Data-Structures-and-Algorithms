
class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children = list()

def printTreeDetailed(root):

    if root is None:
        return

    print(root.data,end=':')
    for child in root.children:
        print(child.data,end=',')
    print()

    for child in root.children:
        printTreeDetailed(child)

def takeinput():

    print('enter root data')
    rootdata = int(input())
    if rootdata == -1:
        return
    root = TreeNode(rootdata)

    print('enter no of children for:',rootdata)
    childcount = int(input())
    for child in range(childcount):
        childNode = takeinput()
        root.children.append(childNode)

    return root

root = takeinput()
printTreeDetailed(root)

def numNodes(root):
    if root is None:
        return 0

    count = 1
    for child in root.children:
        count = count + numNodes(child)

    return count

print(numNodes(root))
