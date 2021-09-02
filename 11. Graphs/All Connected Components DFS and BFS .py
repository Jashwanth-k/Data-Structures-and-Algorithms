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

    def __DFSHelper(self,sv,l,visited):
        l.append(sv)
        visited[sv] = True

        for i in range(self.nVertices):
            if self.containsEdge(sv,i) and visited[i] is False:
                self.__DFSHelper(i,l,visited)

        return l

    def allConnectedDFS(self):
        visited = [False]*self.nVertices
        finalList = []

        for i in range(self.nVertices):
            if visited[i] is False:
                l = []                       #list l must be updated after every call
                l = self.__DFSHelper(i,l,visited)
                if l != None:
                    finalList.append(l)

        return finalList

    def __BFSHelper(self,sv,l,visited):
        q = queue.Queue()
        q.put(sv)
        visited[sv] = True

        while not(q.empty()):
            front = q.get()
            l.append(front)

            for i in range(self.nVertices):
                if self.containsEdge(front,i) and visited[i] is False:
                    visited[i] = True
                    q.put(i)

        return l

    def allConnectedBFS(self):
        visited = [False]*self.nVertices
        finalList = []

        for i in range(self.nVertices):
            if visited[i] is False:
                l = []
                l = self.__BFSHelper(i,l,visited)
                if l != None:
                    finalList.append(l)

        return finalList

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
print(g.allConnectedBFS())

