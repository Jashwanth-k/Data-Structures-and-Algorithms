
def spanningTree(n, edges):
    def getParent(v):
        if parent[v] == v:
            return v
        parent[v] = getParent(parent[v])
        return parent[v]

    size = [0] * n
    parent = [i for i in range(n)]
    edges.sort(key = lambda x: x[2])
    spanningTreeGraph = []
    totalWt = 0
    for v, e, wt in edges:
        vparent = getParent(v)
        eparent = getParent(e)
        if vparent == eparent:
            continue
        totalWt += wt
        vsize = size[vparent]
        esize = size[eparent]
        if vsize >= esize:
            size[vparent] += 1
            parent[eparent] = vparent
        else:
            size[eparent] += 1
            parent[vparent] = eparent
        spanningTreeGraph.append([v, e, wt])
    return totalWt, spanningTreeGraph

n = 3
edges = [[0,1,2],[1,2,10],[0,2,4]]
print(spanningTree(n, edges))
