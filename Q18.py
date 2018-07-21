class Solution(object):
    def fourSum(self, nums, target):
        res = []
        nums.sort()
        for i in xrange(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l < len(nums) - 2:
                r = len(nums) - 1
                m = l + 1
                while m < r:
                    s = nums[i] + nums[l] + nums[m] + nums[r]
                    if s < target:
                        m += 1
                    elif s > target:
                        r -= 1
                    else:
                        res.append((nums[i], nums[l], nums[m], nums[r]))
                        while m < r and nums[m] == nums[m+1]:
                            m += 1
                        while m < r and nums[r] == nums[r-1]:
                            r -= 1
                        m += 1; r -= 1
                while l < len(nums) - 2 and nums[l] == nums[l+1]:
                    l += 1
                l += 1
        return res
t = Solution()
print t.fourSum([1, 0, -1, 0, -2, 2],0) #[-2,-1,0,0,1,2]