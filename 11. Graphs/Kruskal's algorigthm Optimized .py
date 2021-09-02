
class Edge:
    def __init__(self,sour,desti,wt):
        self.sour = sour
        self.desti = desti
        self.wt = wt

def kruskhal(edges,nVertices):
    parent = [i for i in range(nVertices)]
    edges = sorted(edges,key = lambda edge:edge.wt)
    count = 0
    i = 0
    output = []

    mainedge = edges[0]
    mainparent = parent[mainedge.sour]

#mainparent will be first element of edges(list) source. consider zero in  this case

    while count < (nVertices - 1):
        curredge = edges[i]
        sourparent = parent[curredge.sour]
        destiparent = parent[curredge.desti]

        if sourparent != destiparent:
            output.append(curredge)
            count += 1

            parent[destiparent] = mainparent

        i += 1

    print(parent)

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


