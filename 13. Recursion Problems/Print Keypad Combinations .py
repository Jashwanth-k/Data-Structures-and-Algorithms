
def get_str(d):
    if d < 2:
        return " "
    arr = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
    return str(arr[d])

def keypad(n,output=" "):

    if n == 0:
        print(output)
        return

    lastDigit = n%10         #to get the last digit of given number
    str_of_lastdigtit = get_str(lastDigit)

    for i in range(len(str_of_lastdigtit)):   #iterating bcz at 2 (abc) and at 7 (pqrs) len is different
        keypad(n//10,str_of_lastdigtit[i] + output)

n = int(input())
keypad(n)

