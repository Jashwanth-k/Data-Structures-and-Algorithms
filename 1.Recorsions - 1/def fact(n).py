def fact(n):
    if n == 0:
        return 1
    smallcode = fact(n-1)
    return n * smallcode

n = int(input(':'))
print(fact(n))