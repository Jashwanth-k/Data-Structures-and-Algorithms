#creating dictionaries

a = {"the":2, "a":5, 100:"abc"}
print(type(a))
print(a)

print(len(a))

b = a.copy()

c = dict([ ("the",30),("a",50),(2,3) ])
print(c)

d = dict.fromkeys(['how',12,3],10)
print(d)

