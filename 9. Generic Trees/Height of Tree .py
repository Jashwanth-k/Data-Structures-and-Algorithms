
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

def TreeHeight(root):
    if root is None:
        return 0

    maximum = 0
    for child in root.children:
        maximum = max(maximum,TreeHeight(child))

    return 1 + maximum

print(TreeHeight(root))