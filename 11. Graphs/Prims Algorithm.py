import sys
class Graph:
    def __init__(self,nVertices):
        self.nVertices = nVertices
        self.adjMatrix = [[0 for i in range(nVertices)]for j in range(nVertices)]

    def addEdge(self,v1,v2,wt):
        self.adjMatrix[v1][v2] = wt
        self.adjMatrix[v2][v1] = wt

    def __getMinvertex(self,visited,weight):

        min_vertex = -1
        for i in range(self.nVertices):
            if visited[i] is False and(min_vertex == -1 or weight[min_vertex] > weight[i]):
                min_vertex = i

        return min_vertex

    def prims(self):
        visited = [False for i in range(self.nVertices)]
        parent = [-1 for i in range(self.nVertices)]
        weight = [sys.maxsize for i in range(self.nVertices)]
        weight[0] = 0

        for i in range(self.nVertices - 1):
            min_vertex = self.__getMinvertex(visited,weight)
            visited[min_vertex] = True

            #explore the neighbours of minvertex which is not visited and
            #update the weight corresponding to them if required

            for j in range(self.nVertices):
                if self.adjMatrix[min_vertex][j] > 0 and visited[j] is False:
                    if weight[j] > self.adjMatrix[min_vertex][j]:
                        weight[j] = self.adjMatrix[min_vertex][j]
                        parent[j] = min_vertex

        for i in range(1,self.nVertices):
            if i < parent[i]:
                print(i,parent[i],weight[i])
            else:
                print(parent[i],i,weight[i])


inputlist = [int(ele) for ele in input().split()]
n,E = inputlist[0],inputlist[1]

g = Graph(n)

for i in range(E):
    l = [int(ele) for ele in input().split()]
    g.addEdge(l[0],l[1],l[2])

g.prims()

