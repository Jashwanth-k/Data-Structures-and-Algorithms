from StackUsingLL import *

s = Stack()

s.push(10)
s.push(20)
s.push(30)
s.push(40)

while s.isEmpty() is False:
    s.pop()

print(s.size())
print(s.isEmpty())