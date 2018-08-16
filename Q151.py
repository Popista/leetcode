class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = s.split()
        l.reverse()
        return " ".join(l)
t = Solution()
print t.reverseWords("  the    sky is blue")