class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s = []
        self.minValue = float("inf")

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.s.append(x)
        self.minValue = min(self.minValue, x)

    def pop(self):
        """
        :rtype: void
        """
        if not self.s:
            return None
        tmp = self.s.pop()
        if self.s:
            self.minValue = min(self.s)
        else:
            self.minValue = float("inf")
        return tmp

    def top(self):
        """
        :rtype: int
        """
        if not self.s:
            return None
        return self.s[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if not self.s:
            return None
        return self.minValue

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()