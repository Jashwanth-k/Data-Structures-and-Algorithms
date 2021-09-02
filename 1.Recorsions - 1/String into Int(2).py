def str_to_int(s):
    l = len(s)
    if l == 1:
        return ord(s[0]) - ord('0')
    b = ord(s[l-1]) - ord('0')
    a = str_to_int(s[:l-1])
    output = (a*10) + b
    return output

s = '00001231'
print(str_to_int(s))