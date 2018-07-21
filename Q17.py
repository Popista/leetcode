class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == None:
            return []
        result = [""]
        digit_map =  {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        temp = []
        for x in digits:
            temp = []
            for y in result:
                for z in digit_map[x]:
                    temp.append(y+z)
                    print y+z
            result = temp
        return temp
t = Solution()
print t.letterCombinations("234")