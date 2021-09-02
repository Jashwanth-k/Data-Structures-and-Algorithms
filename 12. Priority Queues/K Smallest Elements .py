import heapq

def Ksmallest_elements(li,k):

    heapq._heapify_max(li)   #covert li to max_heap
    for i in range(k,len(arr)):
        maxele = heapq._heappop_max(li)    #get the top element of heap
        if maxele > arr[i]:
            li.append(arr[i])
            heapq._siftdown_max(li,0,len(li)-1)    #for arrange in max heap order
        else:
            li.append(maxele)
            heapq._siftdown_max(li,0,len(li)-1)

n = int(input())
arr = [int(ele) for ele in input().split()]
k = int(input())
li = arr[:k]

Ksmallest_elements(li,k)
print(li)
