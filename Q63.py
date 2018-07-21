class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        board = [[1 for _ in range(len(obstacleGrid[0]))] for _ in range(len(obstacleGrid))]
        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                if obstacleGrid[i][j] == 1:
                    board[i][j] = 0
        for i in range(1, len(board)):
            board[i][0] = board[i][0] & board[i-1][0]
        for i in range(1, len(board[0])):
            board[0][i] = board[0][i] & board[0][i-1]
        for i in range(1, len(board)):
            for j in range(1, len(board[0])):
                if obstacleGrid[i][j] == 1:
                    continue
                else:
                    board[i][j] = board[i-1][j] + board[i][j-1]
        return board[-1][-1]
t = Solution()
print t.uniquePathsWithObstacles([
  [0,0,0],
  [1,1,1],
  [0,0,0]
])