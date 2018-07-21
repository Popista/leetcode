class Solution(object):
    ret = []
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        tmp = []
        self.combine(candidates,target,tmp)
        return self.ret

    def combine(self,candidates,target,tmp):
        if target == 0:
            self.ret.append(list(tmp))  # deep copy: list(tmp)
            return
        for i in range(len(candidates)):
            n = target - candidates[i]
            if n >= 0:
                tmp.append(candidates[i])
                self.combine(candidates[i:],n,tmp)
                tmp.pop()
            # else:
            #     return

t = Solution()
print t.combinationSum([3,1,2],5)