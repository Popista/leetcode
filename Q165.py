class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        # for i in range(len(version1)):
        #     if int(version1[i]) != 0:
        #         version1 = version1[i:]
        #         break
        # for i in range(len(version2)):
        #     if int(version2[i]) != 0:
        #         version2 = version2[i:]
        #         break
        version1 = version1.split(".")
        version2 = version2.split(".")
        print version1
        print version2
        i = 0

        while i < len(version1) and i < len(version2):
            if int(version1[i]) < int(version2[i]):
                return -1
            elif int(version1[i]) > int(version2[i]):
                return 1
            else:
                i += 1
                continue
        if i != len(version1):
            for j in range(i, len(version1)):
                if int(version1[j]) != 0:
                    return 1
        if i != len(version2):
            for j in range(i, len(version2)):
                if int(version2[j]) != 0:
                    return -1
        return 0
t = Solution()
print t.compareVersion("1", "1.0")