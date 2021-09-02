def str_to_int(s):
    l = len(s)
    if l == 1:
        return ord(s[0]) - ord('0')

    a = str_to_int(s[1:])
    b = ord(s[0]) - ord('0')
    output = b*(10**(l-1)) + a
    return output

s = ''
print(str_to_int(s))