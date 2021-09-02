import sys
sys.setrecursionlimit(2000)
def fact(n):
    if n == 0:
        return 1
    smalloutput = fact(n-1)
    output = n * smalloutput
    return output

n = 1500
print(fact(n))
