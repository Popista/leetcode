class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        def DFS(queens, dif, sum):
            p = len(queens)
            if p == n:
                ret.append(queens)
                return
            for i in range(n):
                if i not in queens and p-i not in dif and p+i not in sum:
                    DFS(queens+[i],dif+[p-i],sum+[p+i])
        ret = []
        DFS([],[],[])
        return [['.'*i + 'Q' + '.'*(n-i-1) for i in x] for x in ret]
t = Solution()
x = t.solveNQueens(8)
for i in x:
    for j in i:
        print j
    print "\n"