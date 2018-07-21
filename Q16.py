class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        res = 0
        temp = 99999
        for i in xrange(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < target:
                    l +=1
                elif s > target:
                    r -= 1
                else:
                    return target
                if abs(s - target) < temp:
                    temp = abs(s - target)
                    res = s
        return res
t = Solution()
print t.threeSumClosest([-1,0,1,1,55], 3)