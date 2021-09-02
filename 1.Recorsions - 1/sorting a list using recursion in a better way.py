def ListSortedBetter(a,si):
    l = len(a)
    if si == l - 1 or si == l:  # Here si = starting index
        return True
    elif a[si] > a[si+1]:
        return False
    IsListSorted = ListSortedBetter(a,si+1)
    return IsListSorted      # Now IsLiseSorted returns True nor False

a = [1,2,3,4,5]
si = 0
print(ListSortedBetter(a,si))