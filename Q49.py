class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ret = {}
        for i in sorted(strs):
            tmp = tuple(sorted(i))
            ret[tmp] = ret.get(tmp,[]) + [i]
        return ret.values()
t = Solution()
print t.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])