class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        path = path.split("/")
        ret = []
        i = 0
        while i < len(path):
            if path[i] != "":
                if path[i] == '.':
                    i += 1
                    continue
                if path[i] == "..":
                    if len(ret) > 0:
                        ret.pop()
                    i += 1
                    continue
                else:
                    ret.append(path[i])
                    i += 1
            else:
                i += 1
        result = ""
        if len(ret) == 0:
            return "/"
        for i in ret:
            result += "/" + i
        return result
t = Solution()
print t.simplifyPath("///")