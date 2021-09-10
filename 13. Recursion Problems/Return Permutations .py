
def return_permutations(str):

    if len(str) == 0:
        return ' '

    smalloutput = return_permutations(str[1:])
    output = []

    for substr in smalloutput:      #get the elements from smalloutput
        for j in range(len(str)):
            ele = substr[:j] + str[0] + substr[j:]   #add the first elements of str to substr
            output.append(ele)

    return output

str = input() #abc
ans = return_permutations(str)
print(len(ans))
for i in ans:
    print(i)

