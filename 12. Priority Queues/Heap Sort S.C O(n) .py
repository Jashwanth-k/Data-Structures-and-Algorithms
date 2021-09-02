
class priorityQueueNode:
    def __init__(self,value,priority):
        self.value = value
        self.priority = priority

class prioritQueue:
    def __init__(self):
        self.pq = []

    def size(self):
        return len(self.pq)

    def isEmpty(self):
        return self.size() == 0

    def getMin(self):
        if self.isEmpty():
            return None

        return self.pq[0].value

    def __percolateUp(self):
        childIndex = self.size()-1

        while childIndex > 0:
            l = self.pq
            parentIndex = (childIndex - 1)//2

            if l[childIndex].priority < l[parentIndex].priority:
                l[childIndex],l[parentIndex] = l[parentIndex],l[childIndex]
                childIndex = parentIndex
            else:
                break


    def insert(self,value,priority):
        pqNode = priorityQueueNode(value,priority)
        self.pq.append(pqNode)
        self.__percolateUp()

    def __percolateDown(self):
        parentIndex = 0
        leftchildIndex = 2*parentIndex+1
        rightchildIndex = 2*parentIndex+2

        while leftchildIndex < self.size():
            minIndex = parentIndex
            l = self.pq
            if l[leftchildIndex].priority < l[parentIndex].priority:
                minIndex = leftchildIndex
            if rightchildIndex < self.size() and l[rightchildIndex].priority < l[parentIndex].priority:
                minIndex = rightchildIndex

            if parentIndex == minIndex:
                break

            l[parentIndex],l[minIndex] = l[minIndex],l[parentIndex]
            parentIndex = minIndex
            leftchildIndex = 2*parentIndex+1
            rightchildIndex = 2*parentIndex+2


    def removeMin(self):
        ele = self.pq[0].value
        self.pq[0] = self.pq[self.size()-1]
        self.pq.pop()
        self.__percolateDown()
        return ele

p = prioritQueue()

n = int(input())
l = [int(ele) for ele in input().split()]
while len(l) != 0:
    p.insert(l[0],l[0])
    del l[0]

l2 = []
while p.isEmpty() is False:
    l2.append(p.removeMin())

print(l2)

