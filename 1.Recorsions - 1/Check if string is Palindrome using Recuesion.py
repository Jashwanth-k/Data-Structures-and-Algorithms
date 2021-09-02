def helper(s,si,ei):  # si = 0 and ei = length - 1
    if si == ei:  # here length == 1 return True
        return True
    elif s[si] != s[ei]:   #If first and last indexes are != False
        return False
    elif si < ei+1:     # If si < ei True
        return helper(s,si+1,ei-1)
    return True

def check_palin(s):
    l = len(s)
    if l == 0: #if length == 0 then True
        return True
    return helper(s,0,l-1) # if length > 1 calling another function helper

s = 'raceecar'
print(check_palin(s))