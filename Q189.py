class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # for _ in xrange(k):
        #     tmp = nums.pop()
        #     nums.insert(0, tmp)
        nums[:] = nums[len(nums)-k:] + nums[:len(nums)-k]
        print nums
t = Solution()
print t.rotate([1,2,3,4,5,6,7], 3)