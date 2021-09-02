#s1 and s2 are two Stacks

class QueueUsing_2Stacks:
#enqueue = O(n)
#dequeue = O(1)

    def __init__(self):
        self.__s1 = []
        self.__s2 = []
        self.__count = 0

    def enqueue(self,data):
        while len(self.__s1) != 0:
            self.__s2.append(self.__s1.pop())
        self.__s1.append(data)

        while len(self.__s2) != 0:
            self.__s1.append(self.__s2.pop())
        self.__count += 1

    def dequeue(self):
        if self.isEmpty():
            return 'Hey! Queue is Empty!!'
        self.__count -= 1
        return self.__s1.pop()

    def front(self):
        if self.isEmpty():
            return 'Hey! Queue is Empty!!'
        return self.__s1[self.__count-1]

    def size(self):
        return self.__count

    def isEmpty(self):
        return self.__count == 0

q = QueueUsing_2Stacks()

q.enqueue(9)
q.enqueue(5)
q.enqueue(7)

while q.isEmpty() is False:
    print(q.front())
    q.dequeue()

print(q.dequeue())
