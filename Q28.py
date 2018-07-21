class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if haystack == None or needle == None:
            return -1
        if needle == "":
            return 0
        if haystack == "":
            return -1
        i = 0
        while i < len(haystack):
            if haystack[i] == needle[0]:
                count = 1
                index = i + 1
                for j in range(1,len(needle)):
                    if index < len(haystack):
                        if haystack[index] == needle[j]:
                            count += 1
                        else:
                            break
                    index += 1
                if count == len(needle):
                    return i
                i = index - (len(needle) - count)
                print i
            else:
                i += 1
        return -1
t = Solution()
print t.strStr("mississippi","pii")