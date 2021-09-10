

def print_subsequences(str,output):

    if len(str) == 0:
        print(output)
        return

    #don't include 0th char
    print_subsequences(str[1:],output)

    #include 0th char
    newoutput = output + str[0]
    print_subsequences(str[1:],newoutput)

str = 'abc'
print_subsequences(str," ")

