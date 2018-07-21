# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        ret = []
        for i in sorted(intervals, key=lambda i: i.start):
            left, right = i.start, i.end
            node = Interval(left, right)
            if ret and left <= ret[-1].end:
                ret[-1].end = max(right, ret[-1].end)
            else:
                ret.append(node)
        return ret

i1 = Interval(2, 3)
i2 = Interval(4, 5)
i3 = Interval(6, 7)
i4 = Interval(8, 9)
i5 = Interval(1, 10)
input = [i1, i2, i3, i4, i5]
t = Solution()
x = t.merge(input)
for i in x:
    print str(i.start) + " " + str(i.end)