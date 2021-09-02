
class MapNode():
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next = None

class Map:
    def __init__(self):
        self.bucketsSize = 10
        self.buckets = [None for i in range(self.bucketsSize)]
        self.count = 0

    def size(self):
        return self.count

    def getbucketsindex(self,hc):
        return (abs(hc) % (self.bucketsSize))

    def insert(self,key,value):
        hc = hash(key)
        index = self.getbucketsindex(hc)
        head = self.buckets[index]

        while head is not None:
            if head.key == key:
                head.value = value
                return
            head = head.next

        head = self.buckets[index]  #if we need to insert after updating the value on top
        newNode = MapNode(key,value)
        newNode.next = head
        self.buckets[index] = newNode
        self.count += 1

m = Map()
m.insert('hello',10)
print(m.size())
m.insert('zx',3)
print(m.size())
m.insert('hello',20)
print(m.size())

