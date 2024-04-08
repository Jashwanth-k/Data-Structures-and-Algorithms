# union by rank
class DisjointSetUnion:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1]*n
        
    def findParent(self, node):
        if self.parent[node] == node:
            return node
        self.parent[node] = self.findParent(self.parent[node])
        return self.parent[node]

    def union(self, u, v):
        uParent = self.findParent(u)
        vParent = self.findParent(v)
        uSize = self.size[uParent]
        vSize = self.size[vParent]
        if uSize >= vSize:
            self.parent[vParent] = uParent
            self.size[uParent] += self.size[vParent]
        else:
            self.parent[uParent] = vParent
            self.size[vParent] += self.size[uParent]
        return

    def isConnected(self, u, v):
        return self.findParent(u) == self.findParent(v)

n = 7
edges = [[0,1],[1,3],[1,2],[4,5],[5,6]]
query = [[0,1],[1,2],[4,6],[0,3],[0,4],[6,2]]

dsu = DisjointSetUnion(n)
for i,j in edges:
    dsu.union(i,j)
for i,j in query:
    print(dsu.isConnected(i,j))
