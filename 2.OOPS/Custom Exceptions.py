class ZeroDenominatorError(Exception):
    pass
while True:
    try:
        n = int(input('enter The Numerator :'))
        num = int(n)
        n = int(input('enter the Denominator :'))
        denom = int(n)
        if denom == 0:
            raise ZeroDenominatorError
        value = num/denom
        print(value)
        break
    except ValueError:
        print('Numerator and Denominator must be Integers')
    except ZeroDivisionError:
        print('zerodividionerror raised')
    except ZeroDenominatorError:
        print('Denominator should not be Zero')
