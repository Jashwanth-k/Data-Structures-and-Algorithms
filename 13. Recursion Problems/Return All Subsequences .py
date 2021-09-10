
def subsequences(arr):

    if len(arr) == 0:
        l = [" "]
        return l

    smalloutput = subsequences(arr[1:])
    output = smalloutput[:]
    for i in smalloutput:
        output.append(arr[0] + i)
    return output

arr = input()  #input is string
arr = subsequences(arr)
for i in arr:
    print(i)
