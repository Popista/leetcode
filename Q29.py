class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        ret = 0
        positive = (dividend < 0) is (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        while dividend >= divisor:
            tmp, i = divisor, 1
            while dividend >= tmp:
                dividend -= tmp
                ret += i
                i <<= 1   # i = i * 2
                tmp <<= 1
        if not positive:
            ret = 0 - ret
        return min(max(ret,-pow(2,31)),pow(2,31) - 1)
t = Solution()
print t.divide(123,2)