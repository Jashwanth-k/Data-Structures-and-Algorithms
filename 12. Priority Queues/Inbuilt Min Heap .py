#using inbuilt heap as minheap
import heapq

li = [3,1,2,5,4]
heapq.heapify(li)  #to arrange elements in heap order
print(li)

heapq.heappush(li,0)  #to add elements to heap
print(li)

print(heapq.heappop(li))   #to remove min element from heap
print(li)

heapq.heapreplace(li,6)   #to remove top element and add other element at a time
print(li)

