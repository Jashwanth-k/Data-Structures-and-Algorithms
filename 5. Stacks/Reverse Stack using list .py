
def reverse_Stack(s1,s2):
    if len(s1) <= 1:
        return

    while len(s1) != 1:
        s2.append(s1.pop())

    lastElement = s1.pop()

    while len(s2) != 0:
        s1.append(s2.pop())

    reverse_Stack(s1,s2)
    s1.append(lastElement)
    return s1

s1 = [int(ele) for ele in input().split()]
s2 = []
reverse_Stack(s1,s2)

while len(s1) != 0:
    print(s1.pop(),end=' ')