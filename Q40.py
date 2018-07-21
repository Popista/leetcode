class Solution(object):
    ret = []
    length = 0
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        tmp = []
        candidates.sort()
        self.length = len(candidates)
        self.combine(candidates, target, tmp)
        return self.ret

    def combine(self, candidates, target, tmp):
        if target == 0:
            self.ret.append(list(tmp))  # deep copy: list(tmp)
            return
        for i in range(len(candidates)):
            if len(candidates) == self.length and i >= 1:
                if candidates[i] == candidates[i-1]:
                    continue
            n = target - candidates[i]
            if n >= 0:
                tmp.append(candidates[i])
                self.combine(candidates[i+1:], n, tmp)
                tmp.pop()
                # else:
                #     return
        return

t = Solution()
print t.combinationSum2([10,1,2,7,6,1,5], 8)