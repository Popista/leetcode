class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if board == [[]] or len(board) == 0:
            return
        else:
            self.solve(board)

    def solve(self,board):
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if board[i][j] == '.':
                    for c in range(1,10):
                        if self.isValid(board,i,j,c):
                            board[i][j] = str(c)
                            if self.solve(board):
                                return True
                            else:
                                board[i][j] = '.'
                    return False
        return True    #!!!!!!!


    def isValid(self,board,row,col,c):
        c = str(c)
        for i in range(0,9):
            if board[row][i] == c:
                return False
            if board[i][col] == c:
                return False
            if board[3*(row/3)+i/3][3*(col/3)+i%3] == c:
                return False
        return True
board = [[".",".","9","7","4","8",".",".","."],["7",".",".",".",".",".",".",".","."],[".","2",".","1",".","9",".",".","."],[".",".","7",".",".",".","2","4","."],[".","6","4",".","1",".","5","9","."],[".","9","8",".",".",".","3",".","."],[".",".",".","8",".","3",".","2","."],[".",".",".",".",".",".",".",".","6"],[".",".",".","2","7","5","9",".","."]]
t = Solution()
t.solveSudoku(board)
for i in range(len(board)):
    print board[i]