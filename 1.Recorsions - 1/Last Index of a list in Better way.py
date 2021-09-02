def LastIndex(a,x,si):
    l = len(a)
    if si == l:
        return -1
    smallerListOutput = LastIndex(a,x,si+1)
    if smallerListOutput != -1:
        return smallerListOutput
    else:
        if a[si] == x:
            return si
        else:
            return -1

a = [1,2,3,4,5,4]
x = 4
print(LastIndex(a,x,0))