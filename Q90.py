class Solution(object):

    # def subsetsWithDup(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: List[List[int]]
    #     """
    #     ret = [[]]
    #     sorted(nums)
    #     l = 0
    #     for i in range(len(nums)):
    #         if i == 0 or nums[i] != nums[i-1]:
    #             l = len(ret)
    #         for j in range(len(ret)-l, len(ret)):
    #             ret.append(ret[j] + [nums[i]])
    #     return ret
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = [[]]
        sorted(nums)
        for i in range(len(nums)):
            for j in range(0, len(ret)):
                if sorted(ret[j] + [nums[i]]) not in ret:
                    ret.append(sorted(ret[j] + [nums[i]]))
        return ret

t = Solution()
print t.subsetsWithDup([4, 4, 4, 1, 4])