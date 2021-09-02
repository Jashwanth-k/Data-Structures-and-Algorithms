
def __downheapify(arr,i,n):
    parentIndex = i
    leftchildIndex = 2*parentIndex+1
    rightchildIndex = 2*parentIndex+2

    while leftchildIndex < n:
        minIndex = parentIndex
        if arr[minIndex] > arr[leftchildIndex]:
            minIndex = leftchildIndex
        if rightchildIndex < n and arr[minIndex] > arr[rightchildIndex]:
            minIndex = rightchildIndex

        if parentIndex == minIndex:
            break
        arr[parentIndex],arr[minIndex] = arr[minIndex],arr[parentIndex]
        parentIndex = minIndex
        leftchildIndex = 2*parentIndex+1
        rightchildIndex = 2*parentIndex+2
    return

def heapsort(arr):
    #build the heap
    n = len(arr)
    for i in range(n//2-1,-1,-1):
        __downheapify(arr,i,n)

    for i in range(n-1,0,-1):
        arr[0],arr[i] = arr[i],arr[0]
        __downheapify(arr,0,i)

    return
    #Removing n elements from heap and placing them at correct position

arr = [int(ele) for ele in input().split()]
heapsort(arr)

for i in arr[::-1]:
    print(i,end=' ')

