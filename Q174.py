class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        dp = [[0 for _ in range(len(dungeon[0]))] for _ in range(len(dungeon))]
        dp[-1][-1] = max(1, 1 - dungeon[-1][-1])
        for i in range(len(dungeon)-2,-1,-1):
            dp[i][len(dungeon[0])-1] = max(1, dp[i+1][len(dungeon[0])-1] - dungeon[i][len(dungeon[0])-1])
        for i in range(len(dungeon[0])-2,-1,-1):
            dp[len(dungeon)-1][i] = max(1, dp[len(dungeon)-1][i+1] - dungeon[len(dungeon)-1][i])
        for i in range(len(dungeon)-2,-1,-1):
            for j in range(len(dungeon[0])-2,-1,-1):
                b = max(1, dp[i+1][j] - dungeon[i][j])
                r = max(1, dp[i][j+1] - dungeon[i][j])
                dp[i][j] = min(b, r)
        print dp
        return dp[0][0]
t = Solution()
print t.calculateMinimumHP([[1,-3,3],[0,-2,0],[-3,-3,-3]])