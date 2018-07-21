import copy
class Solution(object):
    ret = []
    def test(self, n, k, l, j):
        if len(l) == k:
            l = sorted(l)
            if l not in self.ret:
                self.ret.append(copy.deepcopy(l))
            return
        for i in xrange(j, n+1):
            l.append(i)
            self.test(n, k, l, i+1)
            l.pop()
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        self.test(n, k, [], 1)
        return self.ret
t = Solution()
print t.combine(4, 2)
