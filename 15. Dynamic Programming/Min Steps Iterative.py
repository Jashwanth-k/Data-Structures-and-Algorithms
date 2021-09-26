
def min_steps(n):
    dp = [-1 for i in range(n+1)]
    dp[1] = 0

    for i in range(2,n+1):

        if i % 3 == 0:
            dp[i] = dp[i//3] + 1

        if i % 2 == 0:
            dp[i] = dp[i // 2] + 1

        ans = dp[i-1] + 1
        if dp[i] == -1:
            dp[i] = ans

        dp[i] = min(ans,dp[i])
        #if the value at dp[i] is less than value of dp[i-1]+1 that will be considered

    return dp[n]

n = int(input())
print(min_steps(n))


def min_steps2(n):
    dp = [float('inf') for i in range(n+1)]
    dp[1] = 0

    for i in range(2,n+1):

        if i % 3 == 0:
            dp[i] = dp[i//3] + 1

        if i % 2 == 0:
            dp[i] = dp[i // 2] + 1

        ans = dp[i-1] + 1
        dp[i] = min(ans,dp[i])

    return dp[n]

n = int(input())
print(min_steps2(n))
