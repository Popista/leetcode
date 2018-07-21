class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    for x in range(len(matrix)):
                        if matrix[x][j] != 0:
                            matrix[x][j] = -1
                    for y in range(len(matrix[0])):
                        if matrix[i][y] != 0:
                            matrix[i][y] = -1
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == -10:
                    matrix[i][j] = 0
        return matrix
t = Solution()
print t.setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]])