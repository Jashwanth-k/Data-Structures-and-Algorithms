
def get_str(d):
    if d < 2:
        return " "
    arr = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
    return arr[d]

def return_keypad(n):

    if n == 0:
        l = [""]
        return l

    lastdigit = n % 10
    smalloutput = return_keypad(n//10)
    strlastdigit = get_str(lastdigit)
    output = []

    for i in smalloutput:
        for j in strlastdigit:
            output.append(i + j)

    return output

n = int(input())
a = return_keypad(n)

for i in a:
    print(i)

