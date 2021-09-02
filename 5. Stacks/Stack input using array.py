from StackUsingarray import Stack

s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)

while s.isEmpty() is False:
    print(s.pop())

print(s.size())
print(s.isEmpty())