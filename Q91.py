class Solution(object):

    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s[0] == '0' or len(s) == 0:
            return 0
        t1, t2 = 1, 1
        tmp = 1
        for i in range(1, len(s)):
            tmp = 0
            if s[i] != '0':
                tmp += t2
            if s[i-1] == '1' or (s[i-1] == '2' and s[i] <= '6'):
                tmp += t1
            t1, t2 = t2, tmp
            # print tmp
            # print (str(t1) + " " + str(t2))
        return tmp
t = Solution()
print t.numDecodings("230")