import itertools
class Solution(object):
    ret = []
    def permute1(self,nums,tmp):
        if len(nums) == 0:
            self.ret.append(list(tmp))
        for i in range(len(nums)): #self.ret.append(list(tmp))
            tmp.append(nums[i])
            self.permute1(nums[0:i]+nums[i+1:],tmp)
            tmp.pop()

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        tmp = []
        self.permute1(nums,tmp)
        return self.ret

t = Solution()
print t.permute([1,1,3])

#import itertools
#return list(itertools.permutations(nums))


# def permute(self, nums):
#     def gen(nums):
#         n = len(nums)
#         if n == 0:
#             yield []
#         else:
#             for i in range(n):
#                 for cc in gen(nums[:i] + nums[i + 1:]):
#                     yield [nums[i]] + cc
#
#     return list(gen(nums))