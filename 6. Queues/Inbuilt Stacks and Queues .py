import queue

#inbuilt Stack as list
s = [1,2,3]

s.append(4)
s.append(5)

print(s.pop())
print(s.pop())
print()

#inbuilt queue
q = queue.Queue()

q.put(6)
q.put(3)
q.put(4)

print(q.get())
print(q.qsize())
print(q.empty())
print()

#inbuilt Stack
s = queue.LifoQueue()

s.put(3)
s.put(4)
s.put(5)

while s.empty() is False:
    print(s.get())
