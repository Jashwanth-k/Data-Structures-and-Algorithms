def lastindex(arr,x,si):
    if si == -1 or l == 0:
        return -1
    if arr[si] == x:
        return si
    return lastindex(arr,x,si-1)

arr = [int(i) for i in input('enter numbers with spaces :').split()]
l = len(arr)
print(arr)
x = int(input('enter a number u want to find :'))
print(lastindex(arr,x,l-1))
