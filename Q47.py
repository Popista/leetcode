class Solution(object):

    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        tmp = []
        ret = [[]]
        nums.sort()
        for n in nums:
            tmp = []
            l = len(ret[-1])
            for i in ret:

                for j in range(l, -1, -1):
                    if j < l and i[j] == n:
                        break
                    else:
                        tmp.append(i[0:j] + [n] + i[j:])
            ret = tmp
        return ret


t = Solution()
print t.permuteUnique([])