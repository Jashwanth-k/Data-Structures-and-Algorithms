from Node import *
#count is for calculating length of LL

class Queue:

    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__count = 0

    def enqueue(self,data):
        newNode = Node(data)
        if self.__head is None:
            self.__head = newNode
            self.__tail = newNode
        else:
            self.__tail.next = newNode
            self.__tail = self.__tail.next
        self.__count += 1

    def dequeue(self):
        if self.isEmpty():
            return 'Hey! Queue is Empty!!'

        element = self.__head.data
        self.__head = self.__head.next
        self.__count -= 1
        return element

    def front(self):
        if self.isEmpty():
            return 'Hey! Queue is Empty!!'

        return self.__head.data

    def size(self):
        return self.__count

    def isEmpty(self):
        return self.__count == 0
