import copy
class Solution(object):


    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        r = [[False, []] for _ in range(len(s))]
        for i in range(len(s)):
            for j in range(i+1):
                if s[j:i+1] in wordDict and (j == 0 or r[j-1][0] is True):
                    #print str(s[j:i+1]) + " " + str(j) + " " + str(i)
                    r[i][0] = True
                    r[i][1].append(j)
                    #break
        if r[len(s)-1][0] != True:
            return []
        print r
        dict = {}
        for i in range(len(r)):
            if r[i][0] == True:
                for j in r[i][1]:
                    if j in dict:
                        dict[j].append(i)
                    else:
                        dict[j] = [i]
        print dict
        if 0 not in dict:
            return []

        def getResult(i, tmp):
            if i not in dict:

                t = " ".join(tmp)
                if len(t.replace(" ", "")) != len(s):
                    return
                else:
                    yield t
                    return
            for j in dict[i]:
                tmp.append(s[i:j + 1])
                for solution in getResult(j+1, tmp):
                    yield solution
                tmp.pop()

        return list(getResult(0, []))


t = Solution()
print t.wordBreak("abcd",
["a","abc","b","cd"])