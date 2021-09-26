import sys
sys.setrecursionlimit(10000)

def stair_case(m,dp):

    if m == 0 or m == 1:
        return 1

    if dp[m-1] == -1:
        ans1 = stair_case(m-1,dp)
        dp[m-1] = ans1
    else:
        ans1 = dp[m-1]

    if dp[m - 2] == -1:
        ans2 = stair_case(m - 2, dp)
        dp[m - 2] = ans2
    else:
        ans2 = dp[m - 2]

    return (ans1 + ans2)

m = int(input())
dp = [-1 for i in range(m+1)]
print(stair_case(m,dp))
