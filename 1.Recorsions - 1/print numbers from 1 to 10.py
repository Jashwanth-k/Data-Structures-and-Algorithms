def print_1_to_10(n):
    if n == 0:
        return
    print_1_to_10(n-1)
    print(n)

n = 10
print_1_to_10(n)