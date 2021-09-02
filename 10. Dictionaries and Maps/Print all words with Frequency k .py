
def printWordsfreq(s,k):

    d = {}
    words = s.split()
    for w in words:
        d[w] = d.get(w,0) + 1

    for w in d:
        if d[w] == k:
            print(w)


s = 'this is a word string having many many words'
k = int(input('enter k value:'))
printWordsfreq(s,k)