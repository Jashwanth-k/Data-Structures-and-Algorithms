def sum(n):
    if n == 0:
        return 0
    if n == 1:
        return array[0]
    return array[n-1] + sum(n-1)

array = [1,2,-3,4]
n = len(array)
print(sum(n))