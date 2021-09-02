from StackUsingLL import *
s = Stack()

def Minimum_Brackets(input):

    count = 0
# if length is odd simply return -1 nothing to d0 furthur
    if len(input)%2 != 0:
        return -1

    for i in input:
        if i == '{':
            s.push(i)

        elif i == '}':
            if s.isEmpty():
                s.push(i)

            elif s.isEmpty() is False and s.top() == '{':
                s.pop()

            elif s.isEmpty() is False and s.top() != '}':
                s.push(i)

#this case must be given last after we complete iteration of elements
    while s.isEmpty() is False:
        c1 = s.pop()
        c2 = s.pop()
        if c1 == c2:
            count += 1
        else:
            count += 2

    return count

input = [ele for ele in input()]
print(Minimum_Brackets(input))