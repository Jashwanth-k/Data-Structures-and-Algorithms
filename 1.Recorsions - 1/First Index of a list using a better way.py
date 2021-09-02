def FirstIndexB(a,x,si):
    l = len(a)
    if si == l:
        return -1
    elif a[si] == x:
        return si
    return FirstIndexB(a,x,si+1)


a = [1,2,3,4,3]
print(FirstIndexB(a,3,0))