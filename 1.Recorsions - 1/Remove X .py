
def remove_x(s):

    if len(s) == 0:
        return s

    if s[0] == 'x':
        return '' + remove_x(s[1:])
    else:
        return s[0] + remove_x(s[1:])

s = 'xaxbc'
print(remove_x(s))


