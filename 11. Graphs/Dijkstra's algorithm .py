import sys
class Graph:
    def __init__(self,nVertices):
        self.nVertices = nVertices
        self.adjMatrix = [[0 for i in range(nVertices)]for j in range(nVertices)]

    def addEdge(self,v1,v2,wt):
        self.adjMatrix[v1][v2] = wt
        self.adjMatrix[v2][v1] = wt

    def __getmind(self,visited,distance):

        minVertex = -1
        for i in range(self.nVertices):
            if visited[i] is False and (minVertex == -1 or distance[minVertex] > distance[i]):
                minVertex = i

        return minVertex

    def dijkstra(self):
        visited = [False for i in range(self.nVertices)]
        distance = [sys.maxsize for i in range(self.nVertices)]
        distance[0] = 0

        for i in range(self.nVertices - 1):
            minVertex = self.__getmind(visited,distance)
            visited[minVertex] = True

    #if distance of neighbours > distance from [0] update the distance

            for j in range(self.nVertices):
                if self.adjMatrix[minVertex][j] > 0 and visited[j] is False:
                    if distance[j] > distance[minVertex] + self.adjMatrix[minVertex][j]:
                        distance[j] = distance[minVertex] + self.adjMatrix[minVertex][j]

        for i in range(self.nVertices):
            print(i,distance[i])

inputlist = [int(ele) for ele in input().split()]
n,E = inputlist[0],inputlist[1]

g = Graph(n)

for i in range(E):
    l = [int(ele) for ele in input().split()]
    g.addEdge(l[0],l[1],l[2])

g.dijkstra()

