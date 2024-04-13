
from heapq import *
from collections import *

def dijkstra(n, edges):
    graph = defaultdict(list)
    for u, v, wt in edges:
        graph[u].append((v, wt))
        graph[v].append((u, wt))

    dist = [float('inf')] * n
    dist[0] = 0
    pq = [(0, 0)]
    while len(pq) != 0:
        curDist, node = heappop(pq)
        if curDist > dist[node]:
            continue
        for sib, nxtDist in graph[node]:
            tDist = curDist + nxtDist
            if tDist < dist[sib]:
                dist[sib] = tDist
                heappush(pq, (tDist, sib))
    return dist

n = 3
edges = [[0,1,2],[1,2,1],[0,2,4]]
print(dijkstra(n, edges))
