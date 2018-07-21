import copy
class Solution(object):
    ret = [[]]
    def test(self, nums, l):
        if l not in self.ret:
            self.ret.append(copy.deepcopy(l))
        if len(nums) == 0:
            return
        for i in range(len(nums)):
            l.append(nums[i])
            self.test(nums[i+1:], l)
            l.pop()
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.test(nums, [])
        return self.ret
t = Solution()
print t.subsets([1,2,3])
