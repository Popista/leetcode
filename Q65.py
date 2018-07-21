class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # try:
        #     float(s)
        # except:
        #     return False
        # return True
        s = s.strip()
        numberSeen = False
        pointSeen = False
        eSeen = False
        for i in s:
            if '0' <= i and i <= '9':
                numberSeen = True
            elif i == '.':
                if eSeen or pointSeen:
                    return False
                pointSeen = True
            elif i == 'e':
                if eSeen or not numberSeen:
                    return False
                numberSeen = False
            else:
                return False
        return numberSeen
t = Solution()
print t.isNumber("2e10")