class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        ret = 0
        while n > 0:
            n /= 5
            ret += n
        return ret
t = Solution()
print t.trailingZeroes(25)