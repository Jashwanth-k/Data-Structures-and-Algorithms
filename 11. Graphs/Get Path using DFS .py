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

    def __getpath_dfsHelper(self,v1,v2,visited):

        if self.adjMatrix[v1][v2] > 0:
            l = []
            l.append(v2)
            l.append(v1)
            return l

        for i in range(self.nVertices):
            if self.containsEdge(v1,i) and visited[i] is False:
                visited[i] = True
                ans = self.__getpath_dfsHelper(i,v2,visited)
                if ans is not None:
                    ans.append(v1)
                    return ans

        return None

    def getpath_dfs(self,v1,v2):
        visited = [False]*self.nVertices
        return self.__getpath_dfsHelper(v1,v2,visited)

g = Graph(4)
g.addEdge(0,1)
g.addEdge(0,3)
g.addEdge(1,2)
g.addEdge(2,3)

print(g.getpath_dfs(1,3))

g2 = Graph(7)
g2.addEdge(6,3)
g2.addEdge(5,3)
g2.addEdge(0,1)
g2.addEdge(3,4)

print(g2.getpath_dfs(0,6))

