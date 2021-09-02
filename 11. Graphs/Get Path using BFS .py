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

    def getpath_bfs(self,v1,v2):
        q = queue.Queue()
        visited = [False]*self.nVertices
        q.put(v1)
        parent = {}

        while not(q.empty()):
            front = q.get()
            for i in range(self.nVertices):
                if self.containsEdge(front,i) and visited[i] is False:
                    visited[i] = True
                    q.put(i)
                    parent[i] = front
                    if front == v2:
                        break

        l = []
        l.append(v2)
        while v2 != v1:
            if v2 in parent:  #if v2's is absent in dictionary return None
                l.append(parent[v2])
            else:
                return
            v2 = parent[v2]

        return l

g = Graph(4)
g.addEdge(0,1)
g.addEdge(0,3)
g.addEdge(1,2)
g.addEdge(2,3)

print(g.getpath_bfs(1,3))

g2 = Graph(7)
g2.addEdge(6,3)
g2.addEdge(5,3)
g2.addEdge(0,1)
g2.addEdge(3,4)

print(g2.getpath_bfs(0,6))

