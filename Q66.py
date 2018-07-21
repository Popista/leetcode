class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        mark = 0
        for i in range(len(digits)-1,-1,-1):
            if i == len(digits) - 1:
                digits[i] += 1
            digits[i] = digits[i] + mark
            mark = (digits[i]) / 10
            digits[i] = digits[i] % 10
            if i == 0 and mark > 0:
                digits.append(mark)
                digits = digits[len(digits)-1:] + digits[:len(digits)-1]

        return digits
t = Solution()
print t.plusOne([9,9])