def checkAB(s):
    if len(s) == 0:
        return True
    elif len(s) == 1:
        if s == 'a':
            return True
        else:
            return False
    elif s[0] == 'a':
        return checkAB(s[1:])
    elif s[0] == 'b':
        if s[1] == 'b':
            return checkAB(s[2:])
        else:
            return False
    else:
        return False

s = 'abbaab'
print(checkAB(s))