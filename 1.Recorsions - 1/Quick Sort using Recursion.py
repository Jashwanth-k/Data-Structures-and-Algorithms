def partition(a,si,ei):
    pivot = a[si]
    c = 0
    for i in range(si,ei+1):
        if a[i] < pivot:
            c+=1
    a[si+c],a[si] = a[si],a[si+c]
    pivot_index = si+c

    i = si
    j = ei
    while i < j:
        if a[i] < pivot:
            i+=1
        elif a[j] >= pivot:
            j-=1
        else:
            a[i],a[j] = a[j],a[i]
            i+=1
            j-=1
    return pivot_index

def QuickSort(a,si,ei):
    if si >= ei:
        return

    pivot_index = partition(a,si,ei)
    QuickSort(a,si,pivot_index-1)
    QuickSort(a,pivot_index+1,ei)

a = [6,34,56,21,32,9,7]
QuickSort(a,0,len(a)-1)
print(a)