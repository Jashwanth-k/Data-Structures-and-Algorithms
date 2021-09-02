#here count is for maintaining the length of array
#front is first element of array
class Queue:

    def __init__(self):
        self.__array = []
        self.__front = 0
        self.__count = 0

    def enqueue(self,data):
        self.__array.append(data)
        self.__count += 1

    def dequeue(self):
        if self.isEmpty():
            return 'Hey! Queue is Empty!!'

        element = self.__array[self.__front]
        self.__front += 1
        self.__count -= 1
        return element

    def front(self):
        if self.isEmpty():
            return 'Hey! Queue is Empty!!'

        return self.__array[self.__front]

    def size(self):
        return self.__count

    def isEmpty(self):
        return self.__count == 0