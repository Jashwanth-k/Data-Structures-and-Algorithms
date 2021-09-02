
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
        print(value)
        break
    except ValueError:
        print('Numerator and Denominator must be integers')

    except ZeroDivisionError:
        print('zerodivision error called')

    except ZeroDenominatorError:   #this will not be called it depends upon order of exception called
        print('Denominator must not be zero')

    except:    #default exception must be last of all exceptions
        print('some Exception occured')