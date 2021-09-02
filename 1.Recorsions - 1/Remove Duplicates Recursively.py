def removeDuplicates(s):
    if len(s) == 0 or len(s) == 1:
        return s

    if s[0] == s[1]:
        smallOutput = removeDuplicates(s[2:])
        return s[0] + smallOutput
    else:
        smallOutput = removeDuplicates(s[1:])
        return s[0] + smallOutput

print(removeDuplicates('aabccba'))