class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        ret = []
        stack = []
        heights.append(float("-inf"))
        for i in range(len(heights)):
            x = i
            while stack and heights[i] < stack[-1][1]:
                x, y = stack.pop()
                ret.append(y * (i - x))
            stack.append([x, heights[i]])
        if ret:
            return max(ret)
        else:
            return 0
t = Solution()
print t.largestRectangleArea([])