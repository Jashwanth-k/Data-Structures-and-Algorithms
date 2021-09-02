from StackUsingLL import *

input = [ele for ele in input()]
s = Stack()

def check_redundant(input):
#append all the elements except closing ")"
    for char in input:
        if char != ')':
            s.push(char)

        elif char == ')':
            count = 0
            while s.top() != '(':
                s.pop()
                count += 1

            #here s.top() will be '('
#if count == 1 i.e only one element present between them ex = (b) this can be reduced to "b"

            if count == 0 or count == 1:
                return True
            s.pop()

    return False

print(check_redundant(input))
