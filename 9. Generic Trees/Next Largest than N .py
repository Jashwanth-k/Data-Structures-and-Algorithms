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


inputlist = [int(ele) for ele in input().split()]
root = takeinputLevelWise(inputlist)
printTreeLevelWise(root)

def Next_larger(root,n):

    if root is None:
        return None

    ans = None
    if root.data > n:
        ans = root.data

    for child in root.children:
        temp = Next_larger(child,n)
        if ans == None or temp < ans:
            ans = temp

    return ans

n = int(input('Enter n value:'))
print(Next_larger(root,n))


