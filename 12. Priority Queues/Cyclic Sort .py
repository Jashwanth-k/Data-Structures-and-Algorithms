
def cyclic_sort(a):

    i = 0
    while i < len(a):
        res = a[i]-1   #here res is correct index of a[i]
        if a[res] == a[i]:
            i += 1
        else:
            a[res],a[i] = a[i],a[res]

a = [int(ele) for ele in input().split()]
cyclic_sort(a)
print(a)
