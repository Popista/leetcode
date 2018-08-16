class Solution(object):

    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        nums = set(nums)
        ret = 1
        while len(nums) > 0:
            tmp = 1
            n = nums.pop()
            left = n - 1
            right = n + 1
            while left in nums:
                tmp += 1
                nums.remove(left)
                left = left - 1
            while right in nums:
                tmp += 1
                nums.remove(right)
                right = right + 1
            if tmp > ret:
                ret = tmp
        return ret
t = Solution()
print t.longestConsecutive([100, 4, 200, 1, 3, 2])
