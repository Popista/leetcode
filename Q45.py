class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if l == 1:
            return 0
        ret, i, left, right  = 0, 0, 0, 0
        while right-left+1 > 0:
            ret += 1
            tmp = 0
            i = left
            while i <= right:
                tmp = max(tmp,nums[i]+i)
                if tmp >= l-1:
                    return ret
                i += 1
            right = tmp
            left = i
        return 0

t = Solution()
print t.jump([0])
