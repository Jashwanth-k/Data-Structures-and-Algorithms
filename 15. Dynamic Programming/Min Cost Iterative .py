
def mincost_path(cost,m,n):

    dp = [[float('inf') for j in range(n+1)] for i in range(m+1)]

    for i in range(m-1,-1,-1):

        for j in range(n-1,-1,-1):
            if i == m-1 and j == n-1:   #from special case
                dp[m-1][n-1] = cost[m-1][n-1]
                continue
            dp[i][j] = cost[i][j] + min(dp[i+1][j],dp[i][j+1],dp[i+1][j+1])

    return dp[0][0]

str = input().split()
m,n = int(str[0]),int(str[1])

cost = [[int(ele) for ele in input().split()] for i in range(m)]
print(mincost_path(cost,m,n))

