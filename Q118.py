class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ret = [[1 for _ in range(i)] for i in range(1, numRows + 1)]
        #print ret
        for i in range(numRows):
            for j in range(i+1):
                if j == 0 or j == i:
                    continue
                else:
                    ret[i][j] = ret[i-1][j-1] + ret[i-1][j]
        return ret
t = Solution()
print t.generate(6)
