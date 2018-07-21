class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        roman_map = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
                     (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]
        i = 0
        while i < len(s):
            for x, y in roman_map:
                if s[i:i + 2] == y:
                    i = i + 2
                    result += x
                    break
                if s[i] == y:
                    i = i + 1
                    result += x
                    break
        return result
t = Solution()
print t.romanToInt("MCMXCVI")