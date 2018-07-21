# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        s, e = newInterval.start, newInterval.end
        left = [i for i in intervals if i.end < s]
        right = [i for i in intervals if i.start > e]
        if left + right != intervals:
            s = min(s, intervals[len(left)].start)
            e = max(e, intervals[~len(right)].end)
        return left + [Interval(s, e)] + right
#[1,2],[3,5],[6,7],[8,10],[12,16]
n1 = Interval(1, 2)
n2 = Interval(3, 5)
n3 = Interval(6, 7)
n4 = Interval(8, 10)
n5 = Interval(12, 16)
l = [n1,n2,n4]
a = Interval(4, 9)
t = Solution()
x = t.insert(l,a)
for i in x:
    print str(i.start) + " " + str(i.end)
