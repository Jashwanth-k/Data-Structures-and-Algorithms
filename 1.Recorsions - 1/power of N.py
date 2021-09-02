def power(x,n):
    if n == 0:
        return 0
    return x**n

x = int(input('enter x val:'))
n = int(input('enter n val:'))
print(power(x,n))