class ZeroDenominatorError(ZeroDivisionError): #here denominator calls divisionError since it is parent class
    pass
while True:
    try:
        n = int(input('enter the numerator :'))
        num = int(n)
        n = int(input('enter the denominator :'))
        denom = int(n)
        if denom == 0:
            raise ZeroDenominatorError
        value = num/denom

    except ValueError:
        print('Numerator and Denominator must be integers')
    except ZeroDenominatorError:
        print('Denominator must not be Zero')
    except ZeroDivisionError:
        print('zerodivision error called')
    else:    # else will be executed only when any Exception is not called
        print(value)
        break
    finally:
        print('Exception may or may not be called')