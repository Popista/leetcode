class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) == 0:
            return 0
        ret = 0
        left, right = [0 for _ in range(len(height))],[0 for _ in range(len(height))]
        left[0] = height[0]
        for i in range(1, len(height)):
            left[i] = max(left[i-1], height[i])
        right[len(height)-1] = height[len(height)-1]
        for i in range(len(height)-2, -1, -1):
            right[i] = max(right[i+1], height[i])
        print right
        for i in range(0,len(height)):
            if min(left[i],right[i]) - height[i] > 0:
                ret += min(left[i],right[i]) - height[i]
        return ret
t = Solution()
print t.trap([5,2,1,2,1,5])
