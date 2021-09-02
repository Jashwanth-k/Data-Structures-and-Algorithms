
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
        childIndex = len(self.pq) - 1

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
        l = self.pq

        while True:
            leftchildIndex = 2*(parentIndex) + 1
            rightchildIndex = 2*(parentIndex) + 2
            minleft = minright = float('inf')

            if leftchildIndex < len(l):
                if l[leftchildIndex].priority < l[parentIndex].priority:
                    minleft = l[leftchildIndex].priority

            if rightchildIndex < len(l):
                if l[rightchildIndex].priority < l[parentIndex].priority:
                    minright = l[rightchildIndex].priority

            if minleft == minright == float('inf'): #when parent is at correct position or both leftchild or rightchild doesn't exist break out
                break

            if minleft < minright:
                l[parentIndex],l[leftchildIndex] = l[leftchildIndex],l[parentIndex]
                parentIndex = leftchildIndex
            else:
                l[parentIndex],l[rightchildIndex] = l[rightchildIndex],l[parentIndex]
                parentIndex = rightchildIndex


    def removeMin(self):
        ele = self.pq[0].value
        self.pq[0] = self.pq[self.size()-1]
        self.pq.pop()
        self.__percolateDown()
        return ele

p = prioritQueue()

n = int(input('enter size:'))
for i in range(n):
    l = [int(ele) for ele in input().split()]
    p.insert(l[0],l[1])

while not(p.isEmpty()):
    print(p.removeMin())

