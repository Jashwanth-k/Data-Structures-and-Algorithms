
class MapNode:
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

    def getvalue(self,key):
        hc = hash(key)
        index = self.getbucketsindex(hc)
        head = self.buckets[index]

        while head is not None:
            if head.key == key:
                return head.value
            head = head.next

        return None

    def remove(self,key):
        hc = hash(key)
        index = self.getbucketsindex(hc)
        head = self.buckets[index]
        prev = None

        while head is not None:
            if head.key == key:
                if prev is None:
                    self.buckets[index] = head.next
                else:
                    prev.next = head.next
                self.count -= 1
                return head.data

            prev = head
            head = head.next
        return None

    def loadFactor(self):
        return self.count/self.bucketsSize

    def rehash(self):
        temp = self.buckets
        self.bucketsSize = 2 * self.bucketsSize
        self.buckets = [None for i in range(self.bucketsSize)]
        self.count = 0

        for head in temp:
            while head is not None:
                self.insert(head.key,head.value)
                head = head.next

    def insert(self, key, value):
        hc = hash(key)
        index = self.getbucketsindex(hc)
        head = self.buckets[index]

        while head is not None:
            if head.key == key:
                head.value = value
                return
            head = head.next

        head = self.buckets[index]
        newNode = MapNode(key, value)
        newNode.next = head
        self.buckets[index] = newNode
        self.count += 1

        loadFactor = self.count/self.bucketsSize
        if loadFactor >= 0.7:
            self.rehash()

    def printMap(self):

        #traversing through the list
        for head in self.buckets:
            while head is not None:
                print(head.key,end='')
                head = head.next

m = Map()

'''for i in range(10):
    m.insert('abc' + str(i),i+1)
    print(m.loadFactor())

for i in range(10):
    print('abc'+str(i),m.getvalue('abc' + str(i)))

print(m.size())
'''

s = input()
for i in s:
    m.insert(i,None)

m.printMap()

