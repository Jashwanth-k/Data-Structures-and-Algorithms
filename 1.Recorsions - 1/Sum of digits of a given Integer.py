def sum_of_digits(n):
    if n <= 0:
        return 0
    slice = int(n%10)     # modulus  gives the last element of the integer 'n'
    smallOutput = sum_of_digits(int(n/10))   #This excludes the last element of integer 'n'
    output = slice + smallOutput
    return output

n = 12345
print(sum_of_digits(n))