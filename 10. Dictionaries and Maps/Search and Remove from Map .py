
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

        head = self.buckets[index]
        newNode = MapNode(key,value)
        newNode.next = head
        self.buckets[index] = newNode
        self.count += 1

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
                return head.value

            prev = head
            head = head.next
        return None


m = Map()
m.insert('hello',10)
print(m.getvalue('hello'))
m.insert('zx',300)
m.insert('hello',20)
print('size',m.size())

print(m.getvalue('hello'))
m.remove('hello')
print(m.getvalue('hello'))
print('size',m.size())
print(m.getvalue('zx'))
