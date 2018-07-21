class Solution(object):
    def initList(self):
        l = [0 for _ in range(10)]
        return l
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        if board == [[]]:
            return False
        for i in range(len(board)):
            l = self.initList()
            for j in range(len(board[i])):
                if board[i][j] != '.':

                    l[int(board[i][j])] += 1
                    if l[int(board[i][j])] > 1:
                        return False
        for i in range(len(board)):
            l = self.initList()
            for j in range(len(board[i])):
                if board[j][i] != '.':
                    l[int(board[j][i])] += 1
                    if l[int(board[j][i])] > 1:
                        return False
        i,j = 0,0
        while i < 9:
            while j < 9:
                for x in range(i,i+3):
                    l = self.initList()
                    for y in range(j,j+3):
                        if board[x][y] != '.':
                            l[int(board[x][y])] += 1
                            if l[int(board[x][y])] > 1:
                                return False
                j += 3
            i += 3
            j = 0
        return True
t = Solution()
print t.isValidSudoku([[".",".","5",".",".",".",".",".","6"],[".",".",".",".","1","4",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".","9","2",".","."],["5",".",".",".",".","2",".",".","."],[".",".",".",".",".",".",".","3","."],[".",".",".","5","4",".",".",".","."],["3",".",".",".",".",".","4","2","."],[".",".",".","2","7",".","6",".","."]])