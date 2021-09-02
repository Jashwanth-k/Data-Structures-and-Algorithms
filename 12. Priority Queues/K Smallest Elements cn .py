import heapq

def Ksmallest(arr,k):

    heap = arr[:k]
    heapq._heapify_max(heap)
    n = len(arr)
    for i in range(k,n):
        if heap[0] > arr[i]:
            heapq._heapreplace_max(heap,arr[i])

    return heap

n = int(input())
arr = [int(ele) for ele in input().split()]
k = int(input())

elements = Ksmallest(arr,k)
for i in elements:
    print(i,end=' ')
