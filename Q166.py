class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        sign = 1
        if numerator < 0 and denominator > 0 or numerator > 0 and denominator < 0:
            sign = -1
            if numerator < 0:
                numerator = -1 * numerator
            if denominator < 0:
                denominator = -1 * denominator
        print numerator / float(denominator)
        q = numerator / denominator
        remain = [numerator % denominator]
        print remain
        r = ""
        flag = 0
        while remain[-1] != 0:
            tmp = str(remain[-1] * 10 / denominator)
            print tmp
            tmp2 = remain[-1] * 10 % denominator
            if tmp2 in remain:
                index = remain.index(tmp2)
                s = "(" + r[index:] + tmp + ")"
                r = r[:index] + s
                break
            else:
                remain.append(tmp2)
                r += tmp
        if r != "":
            if sign == -1:
                return "-" + str(q) + "." + r
            else:
                return str(q) + "." + r
        else:
            if sign == -1:
                return "-" + str(q)
            else:
                return str(q)
t = Solution()
print t.fractionToDecimal(1, 1001)