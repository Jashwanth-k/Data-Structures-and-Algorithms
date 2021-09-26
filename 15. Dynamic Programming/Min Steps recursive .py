
def minSteps(n):

    if n == 1:
        return 0

    ans1 = float('inf')    #taken as infinity bcz we are returning min of answers(1,2,3)
    if n % 3 == 0:
        ans1 = 1 + minSteps(n//3)

    ans2 = float('inf')
    if n % 2 == 0:
        ans2 = 1 + minSteps(n//2)

    ans3 = 1 + minSteps(n-1)

    return min(ans1,ans2,ans3)

n = int(input())
print(minSteps(n))

