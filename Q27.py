class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        ret = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[ret] = nums[i]
                ret += 1
        return ret
t = Solution()
print t.removeElement([3,2,2,3],3)