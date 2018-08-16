class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        flag = 0
        ret = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                flag = 1
                ret = nums[i]
                break
        if flag == 1:
            return ret
        else:
            return nums[0]
t = Solution()
print t.findMin([2,2,2])