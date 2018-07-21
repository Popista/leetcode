class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        a = "1"
        for i in range(n-1):
            tmp = ""
            count = 1
            index = 0
            for c in range(len(a)):
                if tmp == "":
                    count = 1
                    index = 0
                    tmp += str(count)
                    tmp += a[c]
                    continue
                if a[c] == tmp[index+1]:
                    count += 1
                    number = str(count)
                    tmp = tmp[:index] + number + tmp[(index+1):]
                if a[c] != tmp[index+1]:
                    index += 2
                    count = 1
                    tmp += str(count)
                    tmp += a[c]
            a = tmp
        return a
t = Solution()
print t.countAndSay(1)