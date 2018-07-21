class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        r = ""
        temp = 0
        result = 0
        for i in range(len(s)):
            mark = 0
            if r == None:
                r = r + s[i]
                temp = 1
            else:
                location = 0
                for j in range(len(r)):
                    if r[j] == s[i]:
                        if temp > result:
                            result = temp
                        location = j + 1
                        temp = len(r) - j
                        r = r[location:] + s[i]
                        mark = 1
                        break;
                if mark == 0:
                    r = r + s[i]
                    temp = temp + 1
        if result == 0 or temp > result:
            result = temp
        return result

t = Solution()
print t.lengthOfLongestSubstring("tmmzuxt")
