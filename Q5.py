class Solution(object):
    maxLen = 0
    lo = 0
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s)<2:
            return s
        for i in range(len(s)-1):
            self.extend(s,i,i)
            self.extend(s,i,i+1)
        return s[self.lo:self.lo+self.maxLen]

    def extend(self, s, j, k):
        while j>=0 and k < len(s) and s[j] == s[k]:
            j-=1
            k+=1
        if self.maxLen < k - j - 1:
            self.lo = j + 1
            self.maxLen = k - j - 1
t = Solution()
print t.longestPalindrome("")