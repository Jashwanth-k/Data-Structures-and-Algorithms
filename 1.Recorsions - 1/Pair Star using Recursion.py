def string(s,n):
    if n == 1:
        return s[0]
    else:
        if s[n-1] == s[n-2]:
            return string(s,n-1) + "*" + s[n-1]
        else:
            return string(s,n-1) + s[n-1]

s = 'hello'
n = len(s)
print(string(s,n))