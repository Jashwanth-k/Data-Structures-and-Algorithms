
class TrieNode:
    def __init__(self, flag = False):
        self.char = [None] * 26
        self.flag = flag

class TrieFunctions:
    def __init__(self):
        self.root = TrieNode()
        pass

    def addNode(self, charStr):
        n = len(charStr)
        rootNode = self.root
        for i in range(n):
            s = charStr[i]
            idx = ord(s) - ord('a')
            flag = False if i != n-1 else True
            if rootNode.char[idx] != None:
                if flag:
                    rootNode.char[idx].flag = True
                rootNode = rootNode.char[idx]
                continue
            rootNode.char[idx] = TrieNode(flag)
            rootNode = rootNode.char[idx]

    def isExistsHelper(self, curStr, isPrefix = False):
        n = len(curStr)
        i = 0
        rootNode = self.root
        while i < n:
            s = curStr[i]
            idx = ord(s) - ord('a')
            if not rootNode.char[idx]:
                return False
            rootNode = rootNode.char[idx]
            i += 1

        if not isPrefix:
            if rootNode.flag == True:
                return True
            return False
        if isPrefix:
            return True

    def isExists(self, curStr):
        return self.isExistsHelper(curStr)

    def isPrefixExists(self, curStr):
        return self.isExistsHelper(curStr, True)

    def printHelper(self, node, curStr = ''):
        if node.flag == True:
            print(curStr)

        for i in range(26):
            if node.char[i] == None:
                continue
            self.printHelper(node.char[i], curStr + chr(ord('a') + i))

    def printNode(self):
        self.printHelper(self.root)

trie = TrieFunctions()
output = []
T = int(input())
for i in range(T):
    oper, word = [ele for ele in input().split()]
    oper = int(oper)
    if oper == 1:
        trie.addNode(word)
    if oper == 2:
        output.append(trie.isExists(word))
    if oper == 3:
        output.append(trie.isPrefixExists(word))
for i in output:
    print(i)

'''
# INPUT
10
1 aaaa
1 aaaaaa
1 bcd
2 aaaaa
3 aaaaa
3 bc
2 bc
1 bc
3 bcda
2 bc

# OUTPUT
false
true
true
false
false
true
'''
