class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        m = n / 2
        dict = {}
        for i in range(len(nums)):

            if nums[i] in dict:
                dict[nums[i]] += 1

            else:
                dict[nums[i]] = 1
            if dict[nums[i]] > m:
                return nums[i]
t = Solution()
print t.majorityElement([2,2,1,1,1,2,2])