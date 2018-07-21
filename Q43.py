class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if len(num1) == 0 or len(num2) == 0:
            return '0'
        if num1 == '0' or num2 == '0':
            return '0'
        ret = [0 for _ in range(len(num1) + len(num2))]
        for i in range(len(num1)-1,-1,-1):
            for j in range(len(num2)-1,-1,-1):
                x, y = i + j, i + j + 1
                sum = int(num1[i]) * int(num2[j])
                sum = sum + ret[y]
                ret[x] += sum / 10
                ret[y] = sum % 10
        result = ''.join(str(e) for e in ret)
        return result.lstrip('0')
t = Solution()
print t.multiply("8","15")