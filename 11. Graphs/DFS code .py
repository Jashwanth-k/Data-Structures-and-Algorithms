
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

    def __dfsHelper(self,sv,visited): #sv is starting vertex

        print(sv,end=' ')
        visited[sv] = True
        for i in range(self.nVertices):
            if self.containsEdge(sv,i) > 0 and visited[i] is False:
                self.__dfsHelper(i,visited)

    def dfs(self):
        visited = [False]*self.nVertices
        self.__dfsHelper(0,visited)

    def takeinputGraph(self,E):

        for i in range(E):
            l = [int(ele) for ele in input().split()]
            i = 0
            j = 1
            if len(l) <= 1:
                break
            g.addEdge(l[i],l[j])


inputlist = [int(ele) for ele in input().split()]
V,E = inputlist[0],inputlist[1]

g = Graph(V)
g.takeinputGraph(E)
g.dfs()


'''g = Graph(5)
g.addEdge(0,1)
g.addEdge(1,3)
g.addEdge(2,4)
g.addEdge(2,3)
'''

