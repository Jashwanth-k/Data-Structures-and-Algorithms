
from collections import *
from heapq import *
def spanningTree(n, edges):
    graph = defaultdict(list)
    for u,v,wt in edges:
        graph[u].append([v, wt])
        graph[v].append([u, wt])

    minHp = [(0, 0, -1)]
    totalwt = 0
    spanningTreeGraph = []
    visited = set()
    while len(minHp) != 0:
        currwt, currNode, parent = heappop(minHp)
        if currNode in visited:
            continue
        totalwt += currwt
        visited.add(currNode)
        spanningTreeGraph.append([parent, currNode, currwt])
        for sib, sibwt in graph[currNode]:
            if sib in visited:
                continue
            heappush(minHp, (sibwt, sib, currNode))
    return totalwt, spanningTreeGraph

n = 3
edges = [[0,1,2],[1,2,10],[0,2,4]]
print(spanningTree(n, edges))
