import copy
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        prev = [triangle[0][0], triangle[0][0], triangle[0][0]]
        cur = [0, 0, 0]
        for i in range(1, len(triangle)):
            for j in range(1, i+2):
                cur[j] = min(prev[j-1]+triangle[i][j-1], prev[j]+triangle[i][j-1])
            prev = copy.deepcopy(cur)
            prev.append(prev[-1])
            prev[0] = prev[1]
            cur = [0 for _ in range(len(prev))]
        return min([i for i in prev[1:len(prev)-1]])


t = Solution()
print t.minimumTotal([[-1],[2,3],[1,-1,-3]])
