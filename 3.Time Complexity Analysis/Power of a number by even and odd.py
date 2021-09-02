def power(x,n):
    if n == 0:
        return 1
    if n == 1:
        return x
    else:
        smalloutput = power(x,n//2)
        if n % 2 == 0:   # if n is even n//2 * n//2
            return smalloutput * smalloutput
        else:            # if n is odd x * n//2 * n//2
            return x * smalloutput * smalloutput

print(power(5,35))