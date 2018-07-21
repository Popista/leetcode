class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a = list(int(i) for i in a)
        b = list(int(i) for i in b)
        if len(a) < len(b):
            a, b = b, a
        mark = 0
        l1, l2 = len(a), len(b)
        for i in range(l1):
            if i < l2:
                a[l1-i-1] += b[l2-i-1] + mark
                mark = a[l1 - i - 1] / 2
                a[l1-i-1] = a[l1-i-1] % 2
            else:
                a[l1-i-1] += mark
                mark = a[l1 - i - 1] / 2
                a[l1-i-1] = a[l1-i-1] % 2
            if i == l1 - 1 and mark > 0:
                a.append(mark)
                a = a[len(a)-1:] + a[:len(a)-1]
        return "".join(str(i) for i in a)
t = Solution()
print t.addBinary("10","11")