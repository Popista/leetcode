class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        i = 0
        localMin = 0
        localMax = 0
        ret = 0
        while i < len(prices):
            while i < len(prices) - 1 and prices[i+1] < prices[i]:
                i += 1
            localMin = prices[i]
            i += 1
            while i < len(prices) - 1 and prices[i+1] > prices[i]:
                i += 1
            if i == len(prices):
                ret += 0
            else:
                localMax = prices[i]
                ret += localMax - localMin
        return ret
t = Solution()
print t.maxProfit([1,2,3,4,5])