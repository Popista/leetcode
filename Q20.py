class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a = [""]
        for c in s:
            if c == ']' or c == ')' or c == '}':
                if (c == ')' and a[len(a) - 1] == '(') or (c == ']' and a[len(a) - 1] == '[') or (c == '}' and a[len(a) - 1] == '{'):
                    a.pop()
                else:
                    return False
            else:
                a.append(c)
        if len(a) == 1:
            return True
        else:
            return False
t = Solution()
print t.isValid("()")