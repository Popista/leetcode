class Solution(object):
    ret = 0
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        def DFS(queens, dif, sum):
            p = len(queens)
            if p == n:
                self.ret += 1
                return
            for i in range(n):
                if i not in queens and p-i not in dif and p+i not in sum:
                    DFS(queens+[i],dif+[p-i],sum+[p+i])

        DFS([],[],[])
        return self.ret
t = Solution()
print t.totalNQueens(1)