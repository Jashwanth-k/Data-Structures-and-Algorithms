
class Graph:
    def __init__(self,nVertices):
        self.nVertices = nVertices
        self.adjMatrix = [[0 for i in range(nVertices)]for i in range(nVertices)] #same as 2D array

    def addEdge(self,v1,v2):
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1

    def removeEdge(self,v1,v2):
        if self.containsEdge(v1,v2) is False:
            return 'Edge is Absent'
        self.adjMatrix[v1][v2] = 0
        self.adjMatrix[v2][v1] = 0
        return 'removed'

    def containsEdge(self,v1,v2):
        return True if self.adjMatrix[v1][v2] > 0 else False

    def __str__(self):
        return str(self.adjMatrix)

    def printBetter(self):
        for i in (self.adjMatrix):
            print(i)

    def takeinputGraph(self):  #to match the input with test cases
        for i in range(self.nVertices):
            l = [int(ele) for ele in input().split()]
            i = 0
            j = 1
            if len(l) <= 1:
                break
            g.addEdge(l[i],l[j])


'''g = Graph(5)
g.addEdge(0,1)
g.addEdge(1,3)
g.addEdge(2,4)
g.printBetter()

print(g.removeEdge(0,1))
print()
g.printBetter()'''

n = int(input('enter no of vertices value:'))
g = Graph(n)
g.takeinputGraph()
g.printBetter()

