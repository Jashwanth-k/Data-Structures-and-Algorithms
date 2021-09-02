def LastIndex(a,x):
    l = len(a)
    if l == 0:
        return -1
    SmallerList = a[1:]
    SmallerListOutput = LastIndex(SmallerList,x)

    if SmallerListOutput != -1:
        return SmallerListOutput + 1
    else:
        if a[0] == x:
            return 0
        else:
            return -1
a = [1,2,3,4,5,6,4]
x = 4
print(LastIndex(a,x))