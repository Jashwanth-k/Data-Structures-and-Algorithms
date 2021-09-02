#time complexity is O(n)
def __downheapify(arr,i,n):

    parentIndex = i
    leftchildIndex = 2*parentIndex+1
    rightchildIndex = 2*parentIndex+2

    while leftchildIndex < n and rightchildIndex < n:
        if arr[parentIndex] < arr[leftchildIndex] or arr[parentIndex] < arr[rightchildIndex]:
            return False
        return True

def check_Maxheap(arr):

    n = len(arr)
    for i in range(n//2-1,-1,-1):
        ans = __downheapify(arr,i,n)
        if ans is False:
            return False
    return True

n = int(input())
arr = [int(ele) for ele in input().split()]
print(check_Maxheap(arr))

