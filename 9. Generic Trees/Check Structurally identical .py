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


inputlist1 = [int(ele) for ele in input().split()]
inputlist2 = [int(ele) for ele in input().split()]

root1 = takeinputLevelWise(inputlist1)
root2 = takeinputLevelWise(inputlist2)
printTreeLevelWise(root1)
printTreeLevelWise(root2)

def check_structure(root1,root2,i=0):

    if root1 is None or root2 is None: #not a base case but Edge case
        return

    if len(root1.children) != len(root2.children):
        return False

    if root1.data != root2.data:
        return False

    while i < len(root1.children):
        if check_structure(root1.children[i],root2.children[i]) == False:
            return False
        i += 1

    return True

print(check_structure(root1,root2))


