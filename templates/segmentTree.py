
class SegmentTreeNode:
    def __init__(self, n):
        self.segmentTree = None
        self.n = n
        if n & n-1 == 0:
            n = n * 2 - 1
        else:
            n = 2 ** (n // 2 + 1) * 2 - 1
        self.segmentTree = [float('inf')] * n
        self.lazy = [0] * n

    def __constructTreeHelper(self, arr, st, ed, pos = 0):
        if st == ed:
            self.segmentTree[pos] = arr[st]
            return arr[st]

        mid = st + (ed - st) // 2
        left = self.__constructTreeHelper(arr, st, mid, 2 * pos + 1)
        right = self.__constructTreeHelper(arr, mid + 1, ed, 2 * pos + 2)
        self.segmentTree[pos] = min(left, right)
        return self.segmentTree[pos]

    def constructTree(self, arr):
        self.__constructTreeHelper(arr, 0, self.n-1)
        print(self.segmentTree)

    def __queryHelper(self, low, high, st, ed, pos = 0):
        if st > high or ed < low:
            return float('inf')
        if st >= low and ed <= high:
            lazyVal = self.lazy[pos]
            if lazyVal != 0:
                self.segmentTree[pos] = lazyVal
                self.lazy[pos] = 0
                if st != ed:
                    self.lazy[2 * pos + 1] = lazyVal
                    self.lazy[2 * pos + 2] = lazyVal
            return self.segmentTree[pos]

        mid = st + (ed - st) // 2
        left = self.__queryHelper(low, high, st, mid, 2 * pos + 1)
        right = self.__queryHelper(low, high, mid + 1, ed, 2 * pos + 2)
        return min(left, right)

    def findQuery(self, low, high):
        return self.__queryHelper(low, high, 0, self.n - 1)

    def __updateHelper(self, low, high, st, ed, val, pos = 0):
        if st > high or ed < low:
            return self.segmentTree[pos]
        if st >= low and ed <= high:
            self.segmentTree[pos] = val
            self.lazy[pos] = val
            return self.segmentTree[pos]

        mid = st + (ed - st) // 2
        left = self.__updateHelper(low, high, st, mid, val, 2 * pos + 1)
        right = self.__updateHelper(low, high, mid + 1, ed, val, 2 * pos + 2)
        self.segmentTree[pos] = min(left, right)
        return self.segmentTree[pos]

    def updateQuery(self, low, high, val):
        self.__updateHelper(low, high, 0, self.n - 1, val)
        print(self.segmentTree)


arr = [0,-1,3,6,7,2]
n = len(arr)
s = SegmentTreeNode(n)
s.constructTree(arr)
queries = [[0,0], [0,2], [1,2], [2,3], [3,3], [2, 5], [3, 4], [0, 5], [4, 4]]
for st,ed in queries:
    res = s.findQuery(st, ed)
    print(f'Q {st}:{ed} -> {res}')

updates = [[[2, 3], 2], [[0,2],-2]]
for [[st,ed], val] in updates:
    print(f"U {st}:{ed} -> {val}")
    s.updateQuery(st, ed, val)

queries = [[2,3],[3,3],[1,2]]
for st,ed in queries:
    res = s.findQuery(st, ed)
    print(f'Q {st}:{ed} -> {res}')

