class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        r = [False for _ in range(len(s))]
        for i in range(len(s)):
            for j in range(i+1):
                if s[j:i+1] in wordDict and (j == 0 or r[j-1] is True):
                    r[i] = True
                    break
        print r
        return r[-1]
t = Solution()
print t.wordBreak("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"])