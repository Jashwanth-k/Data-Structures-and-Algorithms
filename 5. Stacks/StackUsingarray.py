class Stack():
    def __init__(self):
        self.__data = []

    def push(self,item):
        self.__data.append(item)

    def pop(self):
        if self.isEmpty():
            return 'Hey! Stack is Empty!!'
        return self.__data.pop()

    def top(self):
        if self.isEmpty():
            return 'Hey! Stack is Empty!!'
        return self.__data[self.size()-1]

    def size(self):
        return len(self.__data)

    def isEmpty(self):
        return len(self.__data) == 0