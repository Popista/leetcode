class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0 or prices is None:
            return 0
        maxPrice = 0
        minPrice = float("inf")
        ret = 0
        index = 0
        for i in range(len(prices)):
            if prices[i] < minPrice:
                minPrice = prices[i]
                index = i
            if prices[i] > minPrice and i > index:
                maxPrice = prices[i]
                ret = max(ret, maxPrice - minPrice)
        return max(0, ret)
t = Solution()
print t.maxProfit([3,3,5,0,0,3,1,4])