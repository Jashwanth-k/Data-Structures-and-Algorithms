import queue
class Graph:
    def __init__(self,nVertices):
        self.nVertices = nVertices
        self.adjMatrix = [[0 for i in range(nVertices)]for j in range(nVertices)]

    def addEdge(self,v1,v2):
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1

    def removeEdge(self,v1,v2):
        if self.containsEdge(v1,v2) is False:
            return 'Edge is absent'
        self.adjMatrix[v1][v2] = 0
        self.adjMatrix[v2][v1] = 0

    def containsEdge(self,v1,v2):
        return True if self.adjMatrix[v1][v2] > 0 else False

    def __isConnectedHelper(self,sv,visited):

        for i in range(self.nVertices):
            if self.containsEdge(sv,i) and visited[i] is False:
                visited[i] = True
                self.__isConnectedHelper(i,visited)

    def isConnectedDFS(self,sv=0):
        visited = [False]*self.nVertices
        self.__isConnectedHelper(sv,visited)
        for i in visited:
            if i is False:
                return False
        return True

    def isConnectedBFS(self,sv=0):
        q = queue.Queue()
        q.put(sv)
        visited = [False]*self.nVertices

        while not(q.empty()):
            cv = q.get()
            for i in range(self.nVertices):
                if self.containsEdge(cv,i) and visited[i] is False:
                    visited[i] = True
                    q.put(i)

        for i in visited:
            if i == False:
                return False
        return True

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
print(g.isConnectedBFS())

