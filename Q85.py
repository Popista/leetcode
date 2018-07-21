class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if matrix == []:
            return 0
        m, n = len(matrix), len(matrix[0])
        left = [0 for _ in range(n)]
        right = [n for _ in range(n)]
        height = [0 for _ in range(n)]
        ret = 0
        for i in range(m):
            curR, curL = n, 0

            for j in range(n):
                if matrix[i][j] == '1':
                    height[j] += 1
                    left[j] = max(left[j], curL)

                else:
                    height[j] = 0
                    left[j] = 0
                    curL = j+1

            for j in range(n-1, -1, -1):
                if matrix[i][j] == '1':
                    right[j] = min(right[j], curR)
                else:
                    right[j] = n
                    curR = j
            for j in range(n):
                ret = max(ret, (right[j] - left[j]) * height[j])
        return ret
t = Solution()
print t.maximalRectangle([
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
])