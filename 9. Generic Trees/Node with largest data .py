
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

def takeinput():

    print('Enter root data')
    rootdata = int(input())
    if rootdata == -1:
        return None
    root = TreeNode(rootdata)

    print('Enter no of children for :',rootdata)
    childCount = int(input())
    for child in range(childCount):
        childNode = takeinput()
        root.children.append(childNode)

    return root

root = takeinput()
printTree(root)

def largestdata(root):

    if root is None:
        return

    largestNode = root.data
    for child in root.children:
        if largestNode < largestdata(child):
            largestNode = largestdata(child)

    return largestNode

print(largestdata(root))

def largestNodewithdata(root):

    if root is None:
        return

    maxValue = root.data
    for child in root.children:
        maxValue = max(maxValue,largestNodewithdata(child))

    return maxValue



