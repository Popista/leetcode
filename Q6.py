class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        cols = 0
        rows = 0
        rlist = [ "" for c in range(numRows) ]
        if numRows == 1 or len(s) == 1:
            return s
        for i in range(len(s)):
            if cols % (numRows - 1) == 0:
                #print rows
                rlist[rows] = rlist[rows] + s[i]
                if rows == numRows-1:
                    cols += 1
                    if numRows == 2:
                        rows = 0
                    continue
                else:
                    rows += 1
            else:
                print "here"
                rows -= 1
                rlist[rows] = rlist[rows] + s[i]
                cols += 1
                if cols % (numRows - 1) == 0:
                    rows = 0
        result = ""
        print rlist[1]
        for i in range(len(rlist)):
            result = result + rlist[i]
        return result
t = Solution()
print t.convert("ABC", 2)