class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = nums[0]
        maxN, minN = ret, ret
        for i in range(1, len(nums)):
            if nums[i] < 0:
                maxN, minN = minN, maxN
            maxN = max(maxN * nums[i], nums[i])
            minN = min(minN * nums[i], nums[i])
            ret = max(ret, maxN)

        return ret
t = Solution()
print t.maxProduct([-2,0,-1])