import copy
class Solution(object):
    # def maxProfit(self, prices):
    #     # state machine
    #     if prices is None or prices == []:
    #         return 0
    #     s1 = -prices[0]
    #     s2 = float("-inf")
    #     s3 = float("-inf")
    #     s4 = float("-inf")
    #     for i in range(1, len(prices)):
    #         s1 = max(s1, -prices[i])
    #         s2 = max(s2, s1 + prices[i])
    #         s3 = max(s3, s2 - prices[i])
    #         s4 = max(s4, s3 + prices[i])
    #     return max(0, s4)
    def maxProfit(self, prices):
        # f[k, ii] = max(f[k, ii - 1], prices[ii] + f[k - 1, jj]- prices[jj]) {jj in range of[0, ii - 1]}
        #          = max(f[k, ii - 1], prices[ii] + max(f[k - 1, jj] - prices[jj]))
        if prices is None or prices == []:
            return 0
        k = 2
        profit = [[0 for _ in range(len(prices))] for _ in range(k+1)]
        for i in range(1, k+1):
            tmp = profit[i-1][0] - prices[0]
            for j in range(1, len(prices)):
                profit[i][j] = max(profit[i][j-1], tmp + prices[j])
                tmp = max(tmp, profit[i-1][j] - prices[j])
        print profit
        return max(max(profit))
t = Solution()
print t.maxProfit([2,1,2,0,1])