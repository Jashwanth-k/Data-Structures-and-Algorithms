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

    def __dfsHelper(self,sv,visited): #sv is starting vertex

        print(sv)
        visited[sv] = True
        for i in range(self.nVertices):
            if self.containsEdge(sv,i) > 0 and visited[i] is False:
                self.__dfsHelper(i,visited)

    def dfs(self):
        visited = [False]*self.nVertices
        for i in range(self.nVertices):
            if visited[i] is False:
                self.__dfsHelper(i,visited)

    def __BFShelper(self,sv,visited):
        q = queue.Queue()

        q.put(sv)
        visited[sv] = True

        while q.empty() is False:
            cv = q.get()
            print(cv)
            for i in range(self.nVertices):
                if self.containsEdge(cv,i) > 0 and visited[i] is False:
                    q.put(i)
                    visited[i] = True

        return

    def BFS(self):
        visited = [False]*self.nVertices
        for i in range(self.nVertices):
            if visited[i] is False:
                self.__BFShelper(i,visited)


g = Graph(9)
g.addEdge(0,1)
g.addEdge(1,2)
g.addEdge(2,3)
g.addEdge(4,5)
g.addEdge(4,6)
g.addEdge(5,7)
g.addEdge(6,8)

g.BFS()
print()
g.dfs()