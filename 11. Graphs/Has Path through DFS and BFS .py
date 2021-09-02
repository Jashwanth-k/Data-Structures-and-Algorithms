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

    def __has_pathHelper(self,v1,v2,visited):

        if self.adjMatrix[v1][v2] > 0:
            return True

        for a in range(self.nVertices):
            if self.containsEdge(v1,a) and visited[a] is False:
                visited[a] = True
                return self.__has_pathHelper(a,v2,visited)

        return False

    def has_path(self,v1,v2): #by DFS

        visited = [False]*self.nVertices
        return self.__has_pathHelper(v1,v2,visited)

    def has_pathBFS(self,v1,v2): #by BFS
        q = queue.Queue()
        visited = [False]*self.nVertices

        q.put(v1)
        visited[v1] = True

        while q.empty() is False:
            cv = q.get()
            if self.adjMatrix[cv][v2] > 0:
                return True

            for i in range(self.nVertices):
                if self.containsEdge(v1,i) and visited[i] is False:
                    q.put(i)
                    visited[i] = True

        return False

inputlist = [int(ele) for ele in input().split()]
V,E = inputlist[0],inputlist[1]

g = Graph(V)

for i in range(E+1):
    l = [int(ele) for ele in input().split()]
    j = l[0]
    k = l[1]
    if i != E:
        g.addEdge(j,k)
    else:
        print(g.has_path(j,k))

