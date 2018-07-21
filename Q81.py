class Solution(object):
    ret = False
    def test(self, nums, target):
        l = len(nums)
        mid = (l) / 2
        if nums[mid] == target:
            self.ret = True
            return
        i, j = 0, l - 1
        while nums[i] == nums[mid] and i < mid:
            i += 1
        while nums[j] == nums[mid] and j > mid:
            j -= 1
        if i < mid:
            self.test(nums[i:mid], target)
        if j > mid:
            self.test(nums[mid + 1:j + 1], target)
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if nums == []:
            return False
        self.test(nums, target)
        return self.ret
t = Solution()
print t.search([3,1],3)