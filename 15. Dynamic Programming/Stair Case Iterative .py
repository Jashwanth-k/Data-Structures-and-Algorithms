
def stair_case(m):

    if m == 0 or m == 1:
        return 1

    dp = [-1 for i in range(m+1)]
    dp[0] = 1
    dp[1] = 1

    for i in range(2,m+1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[m]

m = int(input())
print(stair_case(m))
