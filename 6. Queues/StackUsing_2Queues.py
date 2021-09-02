import queue

class StackUsing_2Queues:
#push = O(1)
#pop = O(n)
#top = O(n)

    def __init__(self):
        self.__q1 = queue.Queue()
        self.__q2 = queue.Queue()
        self.__count = 0

    def push(self,data):
        self.__q1.put(data)
        self.__count += 1

    def pop(self):
        if self.isEmpty():
            return 'Hey! Stack is Empty!!'

        while self.__q1.qsize() != 1:
            self.__q2.put(self.__q1.get())
        element = self.__q1.get()

        while self.__q2.qsize() != 0:
            self.__q1.put(self.__q2.get())

        self.__count -= 1
        return element

    def top(self):
#this is same as pop() but we need add toped element to queue1
        if self.isEmpty():
            return 'Hey! Stack is Empty!!'

        while self.__q1.qsize() != 1:
            self.__q2.put(self.__q1.get())
        element = self.__q1.get()

        while self.__q2.qsize() != 0:
            self.__q1.put(self.__q2.get())
        self.__q1.put(element)

        return element

    def size(self):
        return self.__count

    def isEmpty(self):
        return self.__count == 0

s = StackUsing_2Queues()

s.push(3)
s.push(5)
s.push(7)
s.push(10)

while s.isEmpty() is False:
    print(s.top())
    s.pop()

print(s.pop())
