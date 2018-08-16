class Solution(object):
    tboard = []
    l1, l2 = 0, 0
    def getBorder(self, board, x, y):
        if x < 0 or y < 0 or x > len(board)-1 or y > len(board[0])-1:
            return
        #board[x][y] = 'X'
        self.tboard[x][y] = 2
        print (str(x) + " " + str(y))
        if x-1 >= 0 and self.tboard[x-1][y] != 2 and board[x-1][y] == 'O':
            self.getBorder(board, x-1, y)
        if x+1 <= len(board)-1 and self.tboard[x+1][y] != 2 and board[x+1][y] == 'O':
            self.getBorder(board, x+1, y)
        if y-1 >= 0 and self.tboard[x][y-1] != 2 and board[x][y-1] == 'O':
            self.getBorder(board, x, y-1)
        if y+1 <= len(board[0])-1 and self.tboard[x][y+1] != 2 and board[x][y+1] == 'O':
            self.getBorder(board, x, y+1)

    def flip(self, board, x, y):
        if x < 0 or y < 0 or x > len(board)-1 or y > len(board[0])-1:
            return
        board[x][y] = 'X'
        self.tboard[x][y] = 1
        if x-1 >= 0 and board[x-1][y] == 'O':
            self.flip(board, x-1, y)
        if x+1 <= len(board)-1 and board[x+1][y] == 'O':
            self.flip(board, x+1, y)
        if y-1 >= 0 and board[x][y-1] == 'O':
            self.flip(board, x, y-1)
        if y+1 <= len(board[0])-1 and board[x][y+1] == 'O':
            self.flip(board, x, y+1)
        return

    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if board == [] or board == [[]]:
            return
        self.l1 = len(board)
        self.l2 = len(board[0])
        self.tboard = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]
        for i in range(len(board[0])):
            if self.tboard[0][i] != 2:
                if board[0][i] == 'O':
                    self.getBorder(board, 0, i)
            if self.tboard[len(board)-1][i] != 2:
                if board[len(board)-1][i] == 'O':
                    self.getBorder(board, len(board)-1, i)
        for i in range(len(board)):
            if self.tboard[i][0] != 2:
                if board[i][0] == 'O':
                    self.getBorder(board, i, 0)
            if self.tboard[i][len(board[0])-1] != 2:
                if board[i][len(board[0])-1] == 'O':
                    self.getBorder(board, i, len(board[0])-1)

        for i in range(1, len(board)-1):
            for j in range(1, len(board[0])-1):
                if self.tboard[i][j] == 0 and board[i][j] == 'O':
                    self.flip(board, i, j)

        print self.tboard
        print board
t = Solution()
print t.solve([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]])
