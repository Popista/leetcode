# Definition for a point.
class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution(object):
    def category(self, p1, p2):
        if p1[0] == 0 and p2[0] == 0:
            return True
        elif p1[1] == 0 and p2[1] == 0:
            return True
        elif p1[0] != 0 and p1[1] != 0 and p2[0] != 0 and p2[1] != 0:
            if p1[0] / float(p2[0]) == p1[1] / float(p2[1]):
                #print "sss" + str(p1[0] / p2[0])
                return True
            else:
                return False
        else:
            return False
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        dp1 = [[[0, 0] for _ in range(len(points) + 1)] for _ in range(len(points) + 1)]
        dp2 = [[0 for _ in range(len(points) + 1)] for _ in range(len(points) + 1)]
        for i in range(1, len(dp1)):
            for j in range(i+1, len(dp1)):
                # dp2[i][j] = 1
                dp1[i][j][0] = points[i-1].x - points[j-1].x
                dp1[i][j][1] = points[i-1].y - points[j-1].y
                # if dp1[i-1][j][0] == dp1[i][j][0] and dp1[i-1][j][1] == dp1[i][j][1] or dp1[i-1][j][0] == -dp1[i][j][0] and dp1[i-1][j][1] == -dp1[i][j][1]:
                #     dp2[i][j] = max(dp2[i][j], 1 + dp2[i-1][j])
                # if dp1[i][j-1][0] == dp1[i][j][0] and dp1[i][j-1][1] == dp1[i][j][1] or dp1[i][j-1][0] == -dp1[i][j][0] and dp1[i][j-1][1] == -dp1[i][j][1]:
                #     dp2[i][j] = max(dp2[i][j], 1 + dp2[i][j-1])
        # for i in range(1, len(dp1)):
        #     print dp1[i]
        dict = {}
        for i in range(1, len(dp1)):
            for j in range(i + 1, len(dp1)):
                t = Point(dp1[i][j][0], dp1[i][j][1])
                if t in dict:
                    dict[t] += 1
                else:
                    flag = 0
                    for z in dict:
                        if self.category([z.x, z.y], dp1[i][j]):
                            #print str(z.x) + " " + str(z.y) + "s:" + str(dp1[i][j])
                            dict[z] += 1
                            flag = 1
                            break
                    if flag == 0:
                        #print str(t.x) + " " + str(t.y)
                        dict[t] = 1
        ret = float("-inf")
        for i in dict:
            if dict[i] > ret:
                ret = dict[i]
            print str(i.x) + " " + str(i.y) + " " + str(dict[i])
        return ret / 2

t = Solution()
# [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
p1 = Point(1,1)
p2 = Point(2,2)
p3 = Point(100,101)
p4 = Point(4,1)
p5 = Point(2,3)
p6 = Point(1,4)
p = [p1,p2,p3]
print t.maxPoints(p)