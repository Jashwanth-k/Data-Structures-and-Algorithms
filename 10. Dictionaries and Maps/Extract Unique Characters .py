
def unique_char(s):

    d = {}
    for i in s:
        d[i] = d.get(i,0) + 1

    print(d)
    for key in d:
        print(key,end='')

s = input()
unique_char(s)

