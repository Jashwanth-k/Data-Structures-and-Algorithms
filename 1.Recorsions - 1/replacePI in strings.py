def replacePI(s):
    if len(s) == 0 or len(s) == 1:
        return s

    if s[0] == 'p' and s[1] == 'i':
        smallOutput = replacePI(s[2:])
        return '3.14' + smallOutput
    else:
        smallOutput = replacePI(s[1:])
        return s[0] + smallOutput

print(replacePI('pspice'))