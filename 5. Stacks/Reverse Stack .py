from StackUsingLL import *

s1 = Stack()
s2 = Stack()

s1.push(1)
s1.push(2)
s1.push(3)
s1.push(4)

#here the top element is '4' since added last to the Stack

def reverse_Stack(s1,s2):
    if s1.size() <= 1:
        return s1

    for i in range(s1.size()-1):
        s2.push(s1.top())
        s1.pop()

    element = s1.top()
    s1.pop()

    for j in range(s2.size()):
        s1.push(s2.top())
        s2.pop()

    s1 = reverse_Stack(s1,s2)
    s1.push(element)

    return s1

s1 = (reverse_Stack(s1,s2))

#now the last element is '1' since Stack is reversed

while s1.isEmpty() is False:
    print(s1.pop(),end=' ')
