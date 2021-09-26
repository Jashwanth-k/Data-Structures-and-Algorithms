import sys
sys.setrecursionlimit(10000)

#using extra row and column in dp array to for bounds > length
def mincost_path2(arr,i=0,j=0):

    m = len(arr)
    n = len(arr[0])

    if i == m-1 and j == n-1:
        return arr[i][j]

    if i >= m or j >= n:
        return float('inf')

    if dp[i+1][j] == float('-inf'):
        ans1 = mincost_path2(arr,i+1,j)
        dp[i+1][j] = ans1
    else:
        ans1 = dp[i+1][j]

    if dp[i][j+1] == float('-inf'):
        ans2 = mincost_path2(arr,i,j+1)
        dp[i][j+1] = ans2
    else:
        ans2 = dp[i][j+1]

    if dp[i+1][j+1] == float('-inf'):
        ans3 = mincost_path2(arr,i+1,j+1)
        dp[i+1][j+1] = ans3
    else:
        ans3 = dp[i+1][j+1]

    output = arr[i][j] + min(ans1,ans2,ans3)
    return output


str = input().split()
m,n = int(str[0]),int(str[1])

arr = [[int(ele) for ele in input().split()] for i in range(m)]
dp = [[float('-inf') for j in range(n+1)] for i in range(m+1)]
print(mincost_path2(arr))


#using if conditions for bounds > length
def mincost_path(cost,m,n,dp,i=0,j=0):
    if i == m-1 and j == n-1:
        return cost[i][j]

    ans1 = float('inf')
    if i + 1 < m:
        if dp[i+1][j] == float('-inf'):
            ans1 = mincost_path(cost,m,n,dp,i+1,j)
            dp[i+1][j] = ans1
        else:
            ans1 = dp[i+1][j]

    ans2 = float('inf')
    if j + 1 < n:
        if dp[i][j+1] == float('-inf'):
            ans2 = mincost_path(cost,m,n,dp,i,j+1)
            dp[i][j+1] = ans2
        else:
            ans2 = dp[i][j+1]

    ans3 = float('inf')
    if i + 1 < m and j + 1 < n:
        if dp[i+1][j+1] == float('-inf'):
            ans3 = mincost_path(cost,m,n,dp,i+1,j+1)
            dp[i+1][j+1] = ans3
        else:
            ans3 = dp[i+1][j+1]

    output = cost[i][j] + min(ans1,ans2,ans3)
    return output


str = input().split()
m,n = int(str[0]),int(str[1])

cost = [[int(ele) for ele in input().split()] for i in range(m)]
dp = [[float('-inf') for j in range(n)] for i in range(m)]

print(mincost_path(cost,m,n,dp))
