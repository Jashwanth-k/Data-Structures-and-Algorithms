#using bottom up approach

def LCS(str1,str2):

    m = len(str1)
    n = len(str2)

    dp = [[0 for j in range(n+1)] for i in range(m+1)]

    for i in range(m-1,-1,-1):
        for j in range(n-1,-1,-1):
            if str1[i] == str2[j]:
                dp[i][j] = 1 + dp[i+1][j+1]
            else:
                ans1 = dp[i+1][j]
                ans2 = dp[i][j+1]
                dp[i][j] = max(ans1,ans2)

    return dp[0][0]

str1 = input()
str2 = input()
print(LCS(str1,str2))
