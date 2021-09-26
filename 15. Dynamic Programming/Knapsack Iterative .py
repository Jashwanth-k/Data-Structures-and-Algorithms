
def knapsack(weight,value,W):

    n = len(value)

    dp = [[0 for j in range(W+1)] for i in range(n+1)]

    for i in range(n-1,-1,-1):
        for w in range(W+1):
            ans = None
            if weight[i] <= w:
                ans1 = value[i] + dp[i+1][w-weight[i]]
                ans2 = dp[i+1][w]
                ans = max(ans1,ans2)
            else:
                ans = dp[i+1][w]
            dp[i][w] = ans

    return dp[0][W]


n = int(input())
weight = [int(ele) for ele in input().split()]
value = [int(ele) for ele in input().split()]
W = int(input())

print(knapsack(weight,value,W))

