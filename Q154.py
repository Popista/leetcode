class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, len(nums) - 1
        while l < r:
            m = l + (r - l) / 2
            if nums[m] < nums[r]:
                r = m
            elif nums[m] > nums[r]:
                l = m + 1
            else:
                r -= 1
        return nums[l]
t = Solution()
print t.findMin([1,1,2,3,4,4])