import heapq

def __downheapify(i,n):

    parentIndex = i
    leftChildIndex = 2*parentIndex+1
    rightChildIndex = 2*parentIndex+2

    while leftChildIndex < n:
        minIndex = parentIndex
        if arr[minIndex] > arr[leftChildIndex]:
            minIndex = leftChildIndex
        if rightChildIndex < n and arr[minIndex] > arr[rightChildIndex]:
            minIndex = rightChildIndex

        if parentIndex == minIndex:
            break
        arr[parentIndex],arr[minIndex] = arr[minIndex],arr[parentIndex]
        parentIndex = minIndex
        leftChildIndex = 2*parentIndex+1
        rightChildIndex = 2*parentIndex+2
    return

def kth_largest(arr,k):

    heapq.heapify(arr)
    for i in range(len(arr)-1,0,-1):
        arr[0],arr[i] = arr[i],arr[0]
        __downheapify(0,i)

    return arr[k-1]

n = int(input())
arr = [int(ele) for ele in input().split()]
k = int(input())
print(kth_largest(arr,k))

