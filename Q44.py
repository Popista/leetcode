class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if len(p) - p.count("*") > len(s):
            return False
        if (s == "" and p == "*") or (s == "" and p == "") or p == "*":
            return True
        if (s == "" and p != "*") or (s != "*" and p == ""):
            return False
        ret = [[False for _ in range(len(s)+1)] for _ in range(len(p)+1)]
        ret[0][0] = True
        x = 0
        while x < len(p):
            if p[x] == '*':
                for i in range(1,len(s)+1):
                    ret[x+1][i] = ret[x][i] or ret[x][i-1] or ret[x+1][i] or ret[x+1][i-1]
            if p[x] != '*':
                for i in range(0,len(s)):
                    ret[x+1][i+1] = ((ret[x][i])) and (p[x] == s[i] or p[x] == '?')
            ret[x+1][0] = ret[x][0] and p[x] == "*"
            x += 1
        return ret
t = Solution()
a = t.isMatch("c","*?*")
print a



