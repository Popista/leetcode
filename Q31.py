class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        l = len(nums) - 1
        while l > 0 :
            if nums[l-1] < nums[l]:
                break
            l -= 1
        if l == 0:
            nums[:] = nums[::-1]
            return nums
        else:
            r = len(nums) - 1
            l = l - 1
            while r > l:
                if nums[r] > nums[l]:
                    tmp = nums[r]
                    nums[r],nums[l] = nums[l],tmp
                    # nums[r] = nums[l]
                    # nums[l] = tmp
                    break
                r -= 1

            nums[l+1:] = nums[:l:-1]
            return nums
t = Solution()
print t.nextPermutation([1,3,2])