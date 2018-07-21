class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        j = len(height) - 1
        i = 0
        area = 0
        result = 0
        while i < j:
            mark = -1
            if height[i] < height[j]:
                area = (j - i) * height[i]
                mark = 0
            else:
                area = (j - i) * height[j]
                mark = 1
            if area > result:
                result = area
            if mark == 0:
                i += 1
            if mark == 1:
                j -= 1
        return result
t = Solution()
print t.maxArea([1,1])