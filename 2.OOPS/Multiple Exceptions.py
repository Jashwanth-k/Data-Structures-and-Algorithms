while True:
    try:
        n = int(input('enter the Numerator :'))
        num = int(n)
        n = int(input('enter the Denominator :'))
        denom = int(n)
        value = num/denom
        print(value)
        break

    except (ValueError):
        print('Numerator and Denominator must be integers ')
    except (ZeroDivisionError):
        print('Denominator should not be Zero')