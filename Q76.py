import collections
class Solution(object):
    def minWindow(self, s, t):
        need, missing = collections.Counter(t), len(t)
        print need
        i = I = J = 0
        for j, c in enumerate(s, 1):

            missing -= need[c] > 0
            need[c] -= 1
            print need
            if not missing:
                print need[s[i]]
                while i < j and need[s[i]] < 0:
                    need[s[i]] += 1
                    i += 1
                if not J or j - i <= J - I:
                    I, J = i, j
            print need
            print str(i) + " " + str(j)
        return s[I:J]
t = Solution()
print t.minWindow("abcdefggfe", "eg")

