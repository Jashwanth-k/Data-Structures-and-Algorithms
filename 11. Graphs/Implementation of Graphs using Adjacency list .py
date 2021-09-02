
class Node:
    def __init__(self,data,wt):
        self.data = data
        self.wt = wt
        self.next = None

class Graph:
    def __init__(self,nVertices):
        self.nVertices = nVertices
        self.adjlist = [None for i in range(self.nVertices)]

    def addEdge(self,v1,v2,wt):
        newNode = Node(v2,wt)

        if self.adjlist[v1] != None:
            newNode.next = self.adjlist[v1]
        self.adjlist[v1] = newNode

    def removeEdge(self,v1,v2):
        head = self.adjlist[v1]
        prev = None

        while head is not None:
            if head.data == v2:
                if prev is None:
                    self.adjlist[v1] = head.next
                else:
                    prev.next = head.next

            prev = head
            head = head.next

        return

    def containsEdge(self,v1,v2):

        head = self.adjlist[v1]
        while head is not None:
            if head.data == v2:
                return True
            head = head.next
        return False

    def printlist(self):
        for i in range(self.nVertices):
            head = self.adjlist[i]

            if head is not None:
                print(i,end='->')
                while head is not None:
                    print('(' + str(head.data) , str(head.wt) + ')',end=' ')
                    head = head.next
                print()


inputlist = [int(ele) for ele in input().split()]
n,E = inputlist[0],inputlist[1]


g = Graph(n)
for i in range(E):
    l = [int(ele) for ele in input().split()]
    if i == E:
        #print(g.containsEdge(l[0],l[1]))
        break
    g.addEdge(l[0],l[1],l[2])

g.printlist()

print()
g.removeEdge(0,1)
g.removeEdge(1,3)
g.removeEdge(3,4)

g.printlist()
