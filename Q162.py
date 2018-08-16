class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + (r - l) / 2
            #print m
            if m == 0 and nums[m] > nums[m+1] or m == len(nums) - 1 and nums[m] > nums[m-1] or nums[m - 1] < nums[m] > nums[m + 1]:
                return m
            elif m != 0 and nums[m] < nums[m-1]:
                r = m - 1
            elif m != len(nums) - 1 and nums[m] < nums[m+1]:
                l = m + 1
        # if m == 0 and nums[m] > nums[m+1]:
        #     return 0
        # if m == len(nums) - 1 and nums[m] > nums[m-1]:
        #     return len(nums) - 1
        return None
t = Solution()
print t.findPeakElement([1])