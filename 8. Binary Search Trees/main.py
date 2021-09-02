import queue
q = queue.Queue()

class BinarysearchTree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
        self.numNodes = 0

    def ispresentHelper(self,root,data):
        if root is None:
            return False

        if root.data == data:
            return True

        elif root.data > data:
            return self.ispresentHelper(root.left,data)
        else:
            return self.ispresentHelper(root.right,data)

    def ispresent(self,data):
        return self.ispresentHelper(self.root,data)

    def printTreeHelper(self,root):
        #will be printing level wise
        if root is None:
            return
        q.put(root)

        while not(q.empty()):
            currNode = q.get()
            print(currNode.data,end=':')

            if currNode.left is not None:
                print('L',currNode.left.data,end=',')
                q.put(currNode.left)
            else:
                print('L'+'-1',end=',')

            if currNode.right is not None:
                print('R',currNode.right.data,end='')
                print()
                q.put(currNode.right)
            else:
                print('R'+'-1',end='')
                print()
        return

    def printTree(self):
        return self.printTreeHelper(self.root)

    def insertHelper(self,root,data):
        if root is None:
            Node = BinarysearchTree(data)
            return Node

        if root.data > data:
            root.left = self.insertHelper(root.left,data)
            return root

        else:
            root.right = self.insertHelper(root.right,data)
            return root

    def insert(self,data):
        self.numNodes += 1
        self.root =  self.insertHelper(self.root,data)

    def minimum(self,root):
        if root is None:
            return float('inf')

        elif root.left is None:
            return root.data

        return self.minimum(root.left)

    def deletedataHelper(self,root,data):
        if root is None:
            return False,None

        elif root.data > data:
            delete,newleftNode = self.deletedataHelper(root.left,data)
            root.left = newleftNode
            return delete,root

        elif root.data < data:
            delete,newrightNode = self.deletedataHelper(root.right,data)
            root.right = newrightNode
            return delete,root

        #if root.data == data
        #root is leaf
        elif root.left == None and root.right == None:
            return True, None

        #root has one child left
        elif root.left == None:
            return True, root.right

        #root has one child right
        elif root.right == None:
            return True, root.left

        else: #children on both sides
            replacemnet = self.minimum(root.right)
            root.data = replacemnet
            delete, newrightNode = self.deletedataHelper(root.right, replacemnet)
            root.right = newrightNode
            return True, root

    def deletedata(self,data):
        deleted,newroot =  self.deletedataHelper(self.root,data)
        if deleted:
            self.numNodes -= 1
        self.root = newroot
        return deleted

    def count(self):
        return self.numNodes

t = BST()

inputlist = [int(ele) for ele in input().split()]
for i in inputlist:
    t.insert(i)

t.printTree()
print(t.count())
print()

t.deletedata(12)
t.printTree()
print(t.count())
