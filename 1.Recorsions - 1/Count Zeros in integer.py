def count_zeros(n):
    if n == 0:
        return 1
    elif n < 10:
        return 0
    elif int(n%10) == 0:
        return 1 + count_zeros(int(n/10))
    return count_zeros(int(n/10))

n = 10320
print(count_zeros(n))