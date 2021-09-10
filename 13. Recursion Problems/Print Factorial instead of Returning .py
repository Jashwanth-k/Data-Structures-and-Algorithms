
def fact(n):
    if n == 0:
        return 1

    output = n * fact(n-1)
    return output

n = int(input())
print(fact(n))

def printFact(n,ans=1):
    if n == 0:
        print(ans)
        return

    ans = ans * n   #build the ans in every recursive call
    printFact(n-1,ans)

n = int(input())
printFact(n)
