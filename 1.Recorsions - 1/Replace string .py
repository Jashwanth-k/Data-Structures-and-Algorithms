
def replace_str(s,a,b):

    for i in range(len(s)):
        if s[i] == a:
            s = s[:i] + b + s[i+1:]  #since strings are immutable slicing is used to replace
        else:
            s = s

    return s

s = input()
print(replace_str(s,'a','x'))
