class Solution(object):
    def is_number(self,s):
        try:
            float(s)
            return True
        except ValueError:
            pass

        try:
            import unicodedata
            unicodedata.numeric(s)
            return True
        except (TypeError, ValueError):
            pass

        return False
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        result = ""
        sign = -1
        if str == "":
            return 0

        if len(str) == 1 and self.is_number(str) == False:
            return 0
        mark = 0
        mark2 = 0
        for i in range(len(str)):
            if str[i] == " " and mark == 0 and mark2 == 0:
                continue
            if self.is_number(str[i]) == False:
                mark2 = 1
                if str[i] != "-" and str[i] != "+":
                    return 0
                if mark == 1:
                    return 0
            if str[i] == "+":
                mark = 1
            if str[i] == "-":
                mark = 1
                sign = i
                continue
            if self.is_number(str[i]):
                for j in range(sign+1,i):
                    if self.is_number(str[j]) == False:
                        sign = -1
                        break
                result = result + str[i]
                k = i + 1
                while k < len(str) and self.is_number(str[k]):
                    result = result + str[k]
                    k += 1
                if sign != -1:
                    result = "-" + result
                result = int(result)
                if result >= pow(2, 31) - 1:
                    return pow(2, 31) - 1
                if result <= -pow(2, 31):
                    return -pow(2, 31)
                return result
t = Solution()
print t.myAtoi(" +2450000")

