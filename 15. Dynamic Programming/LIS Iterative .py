
def lis(li,n):

    dp = [[0 for j in range(2)] for i in range(n+1)]

    for i in range(n-1,-1,-1):
        including_max = 1    #including is taken as 1. bcz we are assuming first ele is included and its lenght is 1

        for j in range(i+1,n):
            if li[j] > li[i]:
                furthur_including_max = dp[j][0]   #at index i values will be in this format (including,overall)
                including_max = max(including_max,1 + furthur_including_max)

        excluding_max = dp[i+1][1]
        overall_max = max(including_max,excluding_max)
        dp[i] = (including_max,overall_max)

    return dp[0][1]

li = [int(ele) for ele in input().split()]
print(lis(li,len(li)))

'''test cases
5 4 11 1 16 8
6 3 1 2 7 0 9
1 2 2
'''
