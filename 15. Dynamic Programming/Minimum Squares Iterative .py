import math

def minSquares(n):

    dp = [-1 for i in range(n+1)]
    dp[0] = 0

    for nbr in range(1,n+1):
        root = int(math.sqrt(nbr))
        ans = float('inf')

        for j in range(1,root+1):
            currAns = 1 + dp[nbr - (j**2)]
            ans = min(ans,currAns)    #should take overall min from all the answers
        dp[nbr] = ans

    return dp[n]

n = int(input())
print(minSquares(n))

#different approach
def minSquares(n):

    dp = [float('inf') for i in range(n + 1)]
    dp[0] = 0

    for nbr in range(1, n + 1):
        root = int(math.sqrt(nbr))

        for j in range(1, root + 1):
            currAns = 1 + dp[nbr - (j ** 2)]
            dp[nbr] = min(dp[nbr], currAns)

    return dp[n]

n = int(input())
print(minSquares(n))
