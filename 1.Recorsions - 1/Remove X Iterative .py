
def remove_x(s,a,b):

    i = 0
    while i < len(s):
        if s[i] == a:
            s = s[:i] + b + s[i+1:]
        else:
            s = s
            i += 1   #i is only incremented when s[i] is not equal to a

    return s

s = input()
print(remove_x(s,'x',''))
