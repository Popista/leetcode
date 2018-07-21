class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        a = [""]
        ret = 0
        for i in range(len(s)):
            if s[i] == ')':
                if a[len(a) - 1] == "":
                    a.append(i)
                else:
                    index = a[len(a) - 1]
                    index = int(index)
                    if s[index] == '(':
                        a.pop()
                    else:
                        a.append(i)
            else:
                a.append(i)
        if len(a) == 1:
            return len(s)
        else:
            l, r = 0, len(s)
            while len(a) != 1:
                l = a[len(a) - 1]
                a.pop()
                ret = max(ret, r-l-1)
                r = l
            ret = max(ret, r)
        return ret
t = Solution()
print t.longestValidParentheses(")()())")
