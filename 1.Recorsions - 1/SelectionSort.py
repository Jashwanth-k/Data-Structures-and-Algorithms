def selectoinsort(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i+1,len(arr)):
            if arr[min] < arr[j]:
                min = j
        arr[min],arr[i] = arr[i],arr[min]
    return arr

arr = []
n = int(input('enter the length of array :'))
for i in range(n):
    x = int(input('enter the element value :'))
    arr.append(x)
print(selectoinsort(arr))