class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums = map(str, nums)
        cmp = lambda a, b: 1 if a + b > b + a else -1
        ret = "".join(sorted(nums, cmp=cmp, reverse=True))
        if int(ret) == 0:
            return "0"
        else:
            return ret
t = Solution()
print t.largestNumber([3,43,48,94,85,33,64,32,63,66])