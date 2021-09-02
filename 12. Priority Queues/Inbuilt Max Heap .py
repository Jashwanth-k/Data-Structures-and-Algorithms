import heapq

li = [3,1,2,5,4]
heapq._heapify_max(li)   #to construct heap
print(li)

print(heapq._heappop_max(li))   #to remove max element from heap
print(li)

heapq._heapreplace_max(li,0)    #to replace max element with given argument
print(li)

#to push the elements to the heap
li.append(5)
heapq._siftdown_max(li,0,len(li)-1)
print(li)


