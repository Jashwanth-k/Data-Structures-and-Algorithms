

def permutations(str):

    if len(str) == 1:
        return str[0]

    smalloutput = permutations(str[1:])
    output = []

    for i in smalloutput:
        if len(str) == 2:       #this is an edge case
            output.append(str[0] + i)
            output.append(i + str[0])
        else:
            output.append(str[0] + i)

    return output

str = input()
output = []
for i in range(len(str)):     #to consider all elements in str
    str = str[i] + str[:i] + str[i+1:]
    ans = permutations(str)   #in case of 'abc' recursive fun return 'abc','acb'
    output.append(ans)

for i in output:
    for j in i:
        print(j)
