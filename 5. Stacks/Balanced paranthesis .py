from StackUsingLL import *

s = Stack()

def isBalanced(string,s):
    
    for char in string:
        if char in '({[':
            s.push(char)

        elif char == ')':
            if s.isEmpty() or s.top() != '(':
                return False
            s.pop()

        elif char == '}':
            if s.isEmpty() or s.top() != '{':
                return False
            s.pop()

        elif char == ']':
            if s.isEmpty() or s.top() != '[':
                return False
            s.pop()

    if s.isEmpty():
        return True

    return False

string = input('enter the string:')
print(isBalanced(string,s))