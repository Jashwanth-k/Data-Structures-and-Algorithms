'''You are given an integer array nums. You are initially positioned at the array's first index,
and each element in the array represents your maximum jump length at that position.
Return true if you can reach the last index, or false otherwise.'''

'''Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.'''

#Brute Force
def minimum_jumps(arr):

    if len(arr) == 1:
        return True

    n = len(arr)
    boolean = [False for i in range(n)]
    boolean[0] = True

    for i in range(n):
        if boolean[i] == False:
            return False

        for j in range(min(n,(i + arr[i])+1)):
            boolean[j] = True

    return True

arr = [3,2,1,0,4]
print(minimum_jumps(arr))

#optimized solution
def minimum_jumps(arr):

    if len(arr) == 1:
        return True

    n = len(arr)
    dist = 0
    for i in range(n):
        dist = max(dist,arr[i])
        if dist == 0 and i != (n-1):
            return False
        dist -= 1

    return True

arr =  [2,3,1,1,4]
print(minimum_jumps(arr))
