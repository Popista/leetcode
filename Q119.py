class Solution(object):
    def getRow(self, rowIndex):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        rowIndex += 1
        ret = [[1 for _ in range(i)] for i in range(1, rowIndex + 1)]
        # print ret
        for i in range(rowIndex):
            for j in range(i + 1):
                if j == 0 or j == i:
                    continue
                else:
                    ret[i][j] = ret[i - 1][j - 1] + ret[i - 1][j]
        return ret[-1]
t = Solution()
print t.getRow(6)