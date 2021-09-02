def checkprime(n,i):
    if n == i:
        return 0
    else:
        if n % i == 0:
            return 1
        else:
            return checkprime(n,i+1)

n = int(input('enter n value :'))

for i in range(2,n+1):
    if checkprime(i,2) == 0:
        print(i,end=' ')
