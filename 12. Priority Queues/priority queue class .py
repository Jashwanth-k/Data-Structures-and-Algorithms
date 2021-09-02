
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

    def insert(self,value,priority):
        pass

    def removeMin(self):
        pass



