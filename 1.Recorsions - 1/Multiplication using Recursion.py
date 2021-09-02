def mul(m,n):
    if n == 0:
        return 0
    smallOutput = mul(m,n-1)
    return m +smallOutput

m = 3
n = 2
print(mul(m,n))