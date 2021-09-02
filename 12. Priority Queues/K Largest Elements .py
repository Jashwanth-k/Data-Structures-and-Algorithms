import heapq
def Klargest_elements(arr,k):

    heap = arr[:k]
    heapq.heapify(heap)      #using min heap
    for i in range(k,len(arr)):
        if heap[0] < arr[i]:       #removing minimum elements from heap
            heapq.heapreplace(heap,arr[i])

    return heap

n = int(input())
arr = [int(ele) for ele in input().split()]
k = int(input())

elements = Klargest_elements(arr,k)
for i in elements:
    print(i,end=' ')
