
def LCSHelper(str1,str2,i,j,dp):

    if i >= len(str1) or j >= len(str2):
        return 0

    if str1[i] == str2[j]:
        if dp[i+1][j+1] == -1:
            smallans = LCSHelper(str1,str2,i+1,j+1,dp)
            dp[i+1][j+1] = smallans
        else:
            smallans = dp[i+1][j+1]
        return 1 + smallans

    if dp[i+1][j] == -1:
        ans1 = LCSHelper(str1,str2,i+1,j,dp)
        dp[i+1][j] = ans1
    else:
        ans1 = dp[i+1][j]

    if dp[i][j+1] == -1:
        ans2 = LCSHelper(str1,str2,i,j+1,dp)
        dp[i][j+1] = ans2
    else:
        ans2 = dp[i][j+1]

    return max(ans1,ans2)

def LCS(str1,str2):

    m = len(str1)
    n = len(str2)

    dp = [[-1 for j in range(n+1)] for i in range(m+1)]    #create a dp 2D array of size m+1,n+1
    return LCSHelper(str1,str2,0,0,dp)

str1 = input()
str2 = input()

print(LCS(str1,str2))
