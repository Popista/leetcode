class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        last = -1
        i = 0
        l = len(nums)
        while i < l:
            if nums[i] != last:
                count = 1
                last = nums[i]
            else:
                count += 1
                if count > 2:
                    nums.remove(last)
                    count -= 1
                    i -= 1

            i += 1
            l = len(nums)
        return len(nums)
t = Solution()
print t.removeDuplicates([0,0,1,1,1,1,2,3,3])
