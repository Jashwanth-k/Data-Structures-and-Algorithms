
class Edge:
    def __init__(self,sour,desti,wt):
        self.sour = sour
        self.desti = desti
        self.wt = wt

def getparent(v,parent):
    if v == parent[v]:
        return v
    return getparent(parent[v],parent)

def kruskhal(edges,nVertices):
    parent = [i for i in range(nVertices)]
    edges = sorted(edges,key = lambda edge:edge.wt)
    count = 0
    i = 0
    output = []

    while count < (nVertices - 1):
        curredge = edges[i]
        sourparent = getparent(curredge.sour,parent)
        destiparent = getparent(curredge.desti,parent)

        if sourparent != destiparent:
            output.append(curredge)
            count += 1

            parent[sourparent] = destiparent

        i += 1

    return output

inputlist = [int(ele) for ele in input().split()]
n = inputlist[0]
E = inputlist[1]
edges = []

for i in range(E):
    l = [int(ele) for ele in input().split()]
    sour = l[0]
    desti = l[1]
    wt = l[2]
    edge = Edge(sour,desti,wt)
    edges.append(edge)

output = kruskhal(edges,n)

for edge in output:
    if edge.sour < edge.desti:
        print(edge.sour,edge.desti,edge.wt)
    else:
        print(edge.sour,edge.desti,edge.wt)


