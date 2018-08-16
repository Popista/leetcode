class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = set(numbers)
        for i in numbers:
            tmp1 = target - i
            tmp2 = i
            if tmp1 in n:
                break
        if tmp1 == tmp2:
            return [numbers.index(tmp2) + 1, numbers.index(tmp1) + 2]
        else:
            return [numbers.index(tmp2) + 1, numbers.index(tmp1) + 1]
t = Solution()
print t.twoSum([0,0,3,4], 7)