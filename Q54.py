class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix == []:
            return []
        m, n = len(matrix), len(matrix[0])
        ret = []
        i, j = 0, 0
        while i < m and j < n:
            for y in range(j, n):
                ret.append(matrix[i][y])
            for x in range(i + 1, m):
                ret.append(matrix[x][n - 1])
            if m - i == 1 or n - j == 1:
                break
            for y in range(n - 2, j - 1, -1):
                ret.append(matrix[m - 1][y])
            for x in range(m - 2, i, -1):
                ret.append(matrix[x][j])
            i += 1
            j += 1
            m -= 1
            n -= 1
        return ret
t = Solution()
# input = raw_input()
# print input
print t.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]])