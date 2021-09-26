
def fib_Iterative(n):
    dp = [-1 for i in range(n+1)]
    dp[0] = 0
    dp[1] = 1
    i = 2
    while i <= n:
        dp[i] = dp[i-1] + dp[i-2]   #through recurrence relation
        i += 1

    return dp[n]

n = int(input())
print(fib_Iterative(n))
