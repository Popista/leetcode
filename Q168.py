class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        x = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        ret = ""
        while n != 0:
            t1 = n / 26
            # if t1 == 0:
            #     break
            t2 = n % 26
            if t2 == 0:
                n = t1 - 1
                ret += "Z"
                continue
            ret += x[t2-1]
            n = t1
            print t1
            print t2
        return ret[::-1]
t = Solution()
print t.convertToTitle(702)