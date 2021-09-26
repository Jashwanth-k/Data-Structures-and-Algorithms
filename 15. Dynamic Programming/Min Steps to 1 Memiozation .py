
def min_steps(n,dp):
    if n == 1:
        return 0

    if dp[n-1] == -1:
        ans1 = min_steps(n-1,dp)   #after getting values from recursion store those values in array
        dp[n-1] = ans1
    else:
        ans1 = dp[n-1]

    ans2 = float('inf')
    if n % 2 == 0:
        if dp[n//2] == -1:
            ans2 = min_steps(n//2,dp)
            dp[n//2] = ans2
        else:
            ans2 = dp[n//2]

    ans3 = float('inf')
    if n % 3 == 0:
        if dp[n//3] == -1:
            ans3 = min_steps(n//3,dp)
            dp[n//3] = ans3
        else:
            ans3 = dp[n//3]

    return 1 + min(ans1,ans2,ans3)

n = int(input())
dp = [-1 for i in range(n+1)]    #array to store ovrelaping problems
print(min_steps(n,dp))
