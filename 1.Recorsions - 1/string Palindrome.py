def helper(s,si,ei):
    if si > ei:
        return True
    elif s[si] != s[ei]:
        return False
    return helper(s,si+1,ei-1)

def check_palin(s):
    l = len(s)
    if l == 0:
        return True
    return helper(s,0,l-1)

s= 'a'
print(check_palin(s))