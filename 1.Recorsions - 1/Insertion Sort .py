
def insertion_sort(a):

    for i in range(1,len(a)):
        temp = a[i]
        j = i-1

        while j >= 0 and a[j] > temp:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = temp   #j+1 is the correct position to insert the least value


arr = [int(ele) for ele in input().split()]
insertion_sort(arr)
print(arr)
