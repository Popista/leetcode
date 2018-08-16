class Solution(object):
    def radixSort(self, nums):
        for i in range(31):
            one = []
            zero = []
            needle = 1 << i
            for j in nums:
                #print str(j & needle) + " " + str(bin(j)) + " " + str(bin(needle)) + " " + str(needle) + " " + str(j)
                if j & needle != 0:
                    one.append(j)
                else:
                    zero.append(j)
            nums = []
            nums += zero
            nums += one
        return nums
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0
        nums = self.radixSort(nums)
        maxGap = float("-inf")
        for i in range(1, len(nums)):
            maxGap = max(nums[i] - nums[i-1], maxGap)
        return maxGap

t = Solution()
print t.maximumGap([1,10,2])