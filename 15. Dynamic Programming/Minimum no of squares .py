
def min_no_sqrs(n):
    if n == 0:
        return 0

    ans = float('inf')
    i = 1
    while i*i <= n:
        currans = 1 + min_no_sqrs(n-i*i)   #recursion + 1 for each step
        ans = min(ans,currans)
        i += 1

    return ans

n = int(input())
print(min_no_sqrs(n))

