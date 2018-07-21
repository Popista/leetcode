class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        if n < 0:
            n = -n
            x = 1/x
        ret = 1
        while n:
            if n & 1:
                ret *= x
            x *= x
            n >>= 1

        return ret
t = Solution()
print t.myPow(2,10)