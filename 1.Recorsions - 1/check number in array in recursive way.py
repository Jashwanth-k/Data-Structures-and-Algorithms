def find(n):
    x = 2
    if n == 0:
        return False
    if x == array[n-1]:
        return True
    return find(n - 1)

array = [9,8,10]
n = len(array)
print(find(n))