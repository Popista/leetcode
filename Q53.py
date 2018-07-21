class Solution:
    # @param A, a list of integers
    # @return an integer
    # 6:57
    def maxSubArray(self, A):
        if not A:
            return 0

        curSum = maxSum = A[0]
        for num in A[1:]:
            if curSum > 0:
                curSum += num
            else:
                curSum = num
            #curSum = max(num, curSum + num)
            maxSum = max(maxSum, curSum)

        return maxSum
t = Solution()
print t.maxSubArray([2,-1,1,1])