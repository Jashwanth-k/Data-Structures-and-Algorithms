class Solution:
    def search(self, pat, txt):
        n = len(txt)
        m = len(pat)
        table = [0] * m
        # build pattern
        i, j = 0, 1
        ct = 0
        while j < m:
            if pat[i] == pat[j]:
                ct += 1
                table[j] = ct
                i += 1
                j += 1
            else:
                if ct > 0:
                    i = 0
                    ct = 0
                else:
                    table[j] = 0
                    j += 1
    
        # algo
        table.insert(0, '#')
        pat = '#' + pat
        result = []
        i = j = 0
        while i < n:
            if txt[i] == pat[j+1]:
                if j == m-1:
                    result.append((i - (m-1)) + 1)
                    i += 1
                    j = table[j+1]
                    continue
                i += 1
                j += 1
            else:
                if j == 0:
                    i += 1
                else:
                    j = table[j]
        return result

