def isSorted(a):
    l = len(a)
    if l == 0 or l == 1:
        return True
    elif a[0] > a[1]:
        return False
    SmallerList = a[1:]
    isSmallerListSorted = isSorted(SmallerList)
    #return isSmallerListSorted    #HERE this line itself returns true and false
    if isSmallerListSorted:
        return True
    else:
        return False

a = [1,2,3,4,5]
print(isSorted(a))