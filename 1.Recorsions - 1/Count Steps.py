def countSteps(n):
    if n == 0 or n == 1:
        return 1
    elif n == 2:
        return 2
    x = (n-1)
    y = (n-2)
    z = (n-3)
    output = countSteps(x) + countSteps(y) + countSteps(z)
    return output

n = 4
print(countSteps(n))