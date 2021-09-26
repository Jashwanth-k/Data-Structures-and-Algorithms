
def LCS(str1,str2,i=0,j=0):

    if i >= len(str1) or j >= len(str2):
        return 0

    if str1[i] == str2[j]:
        return 1 + LCS(str1,str2,i+1,j+1)    #if both are equal there are contributing themselves.length is 1

    ans1 = LCS(str1,str2,i+1,j)
    ans2 = LCS(str1,str2,i,j+1)
    return max(ans1,ans2)

str1 = input()
str2 = input()
print(LCS(str1,str2))
