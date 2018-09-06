class Solution:
    def reverseBits(self, n):
        tmp = "{0:b}".format(n)
        tmp = (32-len(tmp)) * "0" + tmp
        tmp = tmp[::-1]
        # t = n
        # res = []
        # while t > 1:
        #     res.append(t % 2)
        #     t = t / 2
        # res.append(t)   # 1
        # print list(reversed(res))
        return int(tmp, 2)
    def reverseBits2(self, n):
        res = 0
        for i in range(32):
            end = n & 1
            n >>= 1
            res <<= 1
            res |= end
        return res

    cache = {}
    def reverseBytes(self, n):
        a1 = n >> 24 & 255
        a2 = n >> 16 & 255
        a3 = n >> 8 & 255
        a4 = n & 255
        res = 0
        res += self.reverseBits3(a4)
        res <<= 8
        res += self.reverseBits3(a3)
        res <<= 8
        res += self.reverseBits3(a2)
        res <<= 8
        res += self.reverseBits3(a1)
        return res

    def reverseBits3(self, n):
        if n in self.cache:
            return self.cache[n]
        res = 0
        for i in range(8):
            res = (res << 1) + (n & 1)
            n >>= 1
        self.cache[n] = res
        return res
t = Solution()
print t.reverseBytes(43261596)
