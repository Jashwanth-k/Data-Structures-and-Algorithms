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
root = takeinputLevelWise()
printTreeLevelWise(root)

def MaxchildSumHelper(root):
    if root is None:
        return

    TreeNode = sum = root.data

    for child in root.children: # to add root's data and children data
        sum = sum + child.data

    for child in root.children: # to get the individual child's sum through recursion
        xTreeNode,xsum = MaxchildSumHelper(child)

        if xsum > sum:
            return xTreeNode,xsum

    return TreeNode,sum

def MaxChildSum(root):
    ans,sum = MaxchildSumHelper(root)
    return ans

print('Node with max child sum is:',MaxChildSum(root))
