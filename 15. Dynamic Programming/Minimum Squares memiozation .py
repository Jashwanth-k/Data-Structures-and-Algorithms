import math

def minSquares(n,dp):

    if n == 0:
        return 0

    ans = float('inf')
    root = int(math.sqrt(n))   #sqrt of 41 is 6.we need to explore from 1sqr to 6sqr
    for i in range(1,root+1):

        checkValue = n - (i ** 2)
        if dp[checkValue] == -1:
            smallAns = minSquares(checkValue,dp)
            dp[checkValue] = smallAns
            currans = 1 + smallAns

        else:
            currans = 1 + dp[checkValue]

        ans = min(ans,currans)

    return ans

n = int(input())
dp = [-1 for i in range(n+1)]
print(minSquares(n,dp))
