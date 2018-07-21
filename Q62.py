
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        board = [[1 for _ in range(n)] for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                board[i][j] = board[i-1][j] + board[i][j-1]
        return board[-1][-1]
t = Solution()
print t.uniquePaths(100, 100)