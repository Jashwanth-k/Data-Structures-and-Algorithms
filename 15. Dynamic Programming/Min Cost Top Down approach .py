
def mincost_pathTD(cost,m,n):

    dp = [[float('inf') for j in range(n+1)]for i in range(m+1)]

    for i in range(1,m+1):
        for j in range(1,n+1):
            if i == 1 and j == 1:
                dp[i][j] = cost[0][0]
                continue
            dp[i][j] = cost[i-1][j-1] + min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1])

    return dp[m][n]

str = input().split()
m,n = int(str[0]),int(str[1])

cost = [[int(ele) for ele in input().split()] for i in range(m)]
print(mincost_pathTD(cost,m,n))

