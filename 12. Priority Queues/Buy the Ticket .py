import queue
import heapq

def buy_ticket(arr,q,k):

    maxheap = arr[:]
    heapq._heapify_max(maxheap)   #convert the given priorities to maxheap
    time = 0

    while True:
        ele = q.get()
        maxele = heapq._heappop_max(maxheap)   #get the max ele for heap

        if arr[ele] == maxele:
            time += 1
            if ele == k:
                return time

        else:
            q.put(ele)
            maxheap.append(maxele)
            heapq._siftdown_max(maxheap,0,len(maxheap)-1)
    return

n = int(input())
arr = [int(ele) for ele in input().split()]
k = int(input())

q = queue.Queue()
for i in range(len(arr)):
    q.put(i)

print(buy_ticket(arr,q,k))
