
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
        return 'removed'

    def containsEdge(self,v1,v2):
        return True if self.adjMatrix[v1][v2] > 0 else False

    def BFS(self):
        import queue
        q = queue.Queue()

        q.put(0)
        visited = [False]*self.nVertices
        visited[0] = True

        while q.empty() is False:
            sv = q.get()
            print(sv,end=' ')
            for i in range(self.nVertices):
                if self.containsEdge(sv,i) > 0 and visited[i] is False:
                    q.put(i)
                    visited[i] = True

        return

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
g.BFS()


'''g = Graph(7)
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,3)
g.addEdge(1,4)
g.addEdge(2,6)
g.addEdge(4,5)
g.addEdge(5,6)
'''
