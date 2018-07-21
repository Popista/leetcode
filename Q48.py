class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        l1, l2 = len(matrix), len(matrix[0])
        for i in range(l1):
            j = i
            while j < l2 - i - 1:
                x = 0
                tmp = matrix[i][j]
                while x < 4:
                    tmp2 = matrix[j][l1 - 1 - i]
                    matrix[j][l1 - 1 - i] = tmp
                    tmp = tmp2
                    tmp3 = i
                    i = j
                    j = l1 - 1 - tmp3
                    x += 1
                j += 1
        print matrix
        return
t = Solution()
t.rotate([
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
])