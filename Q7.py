class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x >= 0:
            temp = str(x)
            re = temp[::-1]

        else:
            temp = str(x)
            re = temp[:0:-1]
            print re
            re = temp[0] + re

        re = int(re)
        if re >= pow(2,31) - 1:
            return 0
        if re <= -pow(2,31):
            return 0
        return re
t = Solution()
print t.reverse(9000)