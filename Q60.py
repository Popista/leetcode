import math
class Solution(object):

    def getPermutation(self, n, k):
        numbers = range(1, n+1)
        permutation = ''
        k -= 1
        while n > 0:
            n -= 1
            # get the index of current digit
            index, k = divmod(k, math.factorial(n))
            print numbers
            permutation += str(numbers[index])
            # remove handled number
            numbers.remove(numbers[index])

        return permutation
t = Solution()
print t.getPermutation(3,2)
