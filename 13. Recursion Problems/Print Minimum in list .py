
def findmin(arr):

    if len(arr) == 0:
        return float('inf')

    min = arr[0]
    output = findmin(arr[1:])
    if output < min:
        min = output
    return min

arr = [3,4,2,-1,0,9,-2,5]
print(findmin(arr))

def printMin(arr,min=float('inf')):

    if len(arr) == 0:
        print(min)
        return

    if min > arr[0]:
        min = arr[0]
    printMin(arr[1:],min)

printMin(arr)
