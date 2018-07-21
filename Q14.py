class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        index = 0
        minlength = 100000
        for i in range(len(strs)):
            if len(strs[i]) < minlength:
                minlength = len(strs[i])
                index = i
        prefix = strs[index]
        j = len(strs[index])
        i = 0
        while i < len(strs):
            if i == index:
                i += 1
                continue
            if strs[i] == "":
                return ""
            x = 0
            while x < len(prefix[0:j]) and x < len(strs[i]):
                if prefix[x] != strs[i][x]:
                    j = x
                    break
                else:
                    x += 1
            i += 1

        return prefix[0:j]
t = Solution()
print t.longestCommonPrefix(["aac","cab","abb"])