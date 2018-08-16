class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        x = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        l = len(s)
        ret = 0
        for i in range(l):
            ret += (x.index(s[i]) + 1) * 26 ** (l-i-1)
        return ret
t = Solution()
print t.titleToNumber("ZY")