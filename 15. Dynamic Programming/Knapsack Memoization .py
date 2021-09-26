#here we have two unique values that is W w.r.t i at one position.
#we will maintain a 2d array to store values w.r.t W and i

def knapsack(weight,values,W,dp,i=0):

    if i >= len(values):
        return 0

    if weight[i] <= W:
        if dp[W-weight[i]][i] == -1:
            ans1 = values[i] + knapsack(weight, values, W - weight[i],dp, i + 1)
            dp[W-weight[i]][i] = ans1
        else:
            ans1 = dp[W-weight[i]][i]

        if dp[W][i] == -1:
            ans2 = knapsack(weight, values, W,dp, i + 1)
            dp[W][i] = ans2
        else:
            ans2 = dp[W][i]

        ans = max(ans1, ans2)

    else:
        if dp[W][i] == -1:
            ans = knapsack(weight,values,W,dp,i+1)
            dp[W][i] = ans
        else:
            ans = dp[W][i]
    return ans

n = int(input())
weight = [int(ele) for ele in input().split()]
values = [int(ele) for ele in input().split()]
W = int(input())
dp = [[-1 for i in range(n+1)] for j in range(W+1)]

print(knapsack(weight,values,W,dp))

