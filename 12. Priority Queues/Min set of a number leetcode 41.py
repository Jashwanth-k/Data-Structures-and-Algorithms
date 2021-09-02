
def cyclic_sort(a):

    i = 0
    l = []
    while i < len(a):
        res = a[i]-1
        if a[i] > 0 and a[i] < len(a) and a[i] != a[res]:
            a[res],a[i] = a[i],a[res]
        else:
            i += 1

    for i in range(len(a)):
        if a[i] != i+1:
            return i+1
    return len(a)+1

a = [int(ele) for ele in input().split()]
print(cyclic_sort(a))
print(a)
