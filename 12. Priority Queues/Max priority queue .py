
class PriorityQueueNode:
    def __init__(self,value,priority):
        self.value = value
        self.priority = priority

class PriorityQueue:
    def __init__(self):
        self.pq = []

    def getSize(self):
        return len(self.pq)

    def getMax(self):
        return self.pq[self.getSize()-1]

    def isEmpty(self):
        return self.getSize() == 0

    def __porcolateUp(self):
        childIndex = self.getSize()-1

        while childIndex > 0:
            l = self.pq
            parentIndex = (childIndex - 1)//2

            if l[childIndex].priority > l[parentIndex].priority:
                l[parentIndex],l[childIndex] = l[childIndex],l[parentIndex]
                childIndex = parentIndex
            else:
                break

    def insert(self,value,priority):
        pqNode = PriorityQueueNode(value,priority)
        self.pq.append(pqNode)
        self.__porcolateUp()

    def __percolateDown(self):
        parentIndex = 0

        while True:
            minIndex = parentIndex
            l = self.pq
            leftchildIndex = 2*parentIndex+1
            rightchildIndex = 2*parentIndex+2

            if leftchildIndex < self.getSize() and l[leftchildIndex].priority > l[parentIndex].priority:
                minIndex = leftchildIndex
            if rightchildIndex < self.getSize() and l[rightchildIndex].priority > l[minIndex].priority:
                minIndex = rightchildIndex

            if parentIndex == minIndex:
                break
            l[parentIndex],l[minIndex] = l[minIndex],l[parentIndex]
            parentIndex = minIndex


    def removeMax(self):
        ele = self.pq[0].value
        self.pq[0] = self.pq[self.getSize()-1]
        self.pq.pop()
        self.__percolateDown()
        return ele

pq = PriorityQueue()

n = int(input('enter n value:'))
for i in range(n):
    l = [int(ele) for ele in input().split()]
    pq.insert(l[0],l[0])

while not(pq.isEmpty()):
    print(pq.removeMax())

'''pq.insert('A',10)
pq.insert('C',5)
pq.insert('B',19)
pq.insert('D',4)'''
