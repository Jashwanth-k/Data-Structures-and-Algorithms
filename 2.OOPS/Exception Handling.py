while True:
    try:
        n = int(input('enter the numerator :'))
        num = int(n)
        n = int(input('enter the denominator :'))
        denom = int(n)
        value = (num / denom)
        print(value)
        break

    except ValueError:
        print('Numerator and Denominator must be integers')
