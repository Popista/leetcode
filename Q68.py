class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        i = 0
        ret = []
        if words == [""]:
            line = ""
            for _ in range(maxWidth):
                line += " "
            return [line]
        while i < len(words):
            sum = 0
            line = ""
            while i < len(words) and sum < maxWidth:
                sum += len(words[i]) + 1
                line += words[i] + " "
                i += 1
            sum -= 1
            line = line[:len(line)-1]
            if sum == maxWidth:
                ret.append(line)
            elif sum < maxWidth:
                if i < len(words):
                    line = line.split()
                    x = maxWidth - sum + len(line) - 1
                    index = 0
                    while x > 0:
                        if len(line) == 1:
                            line[index] += " "
                        else:
                            line[index] += " "
                            index += 1
                            index = index % (len(line) - 1)
                        x -= 1

                    line2 = "".join(line)
                    print len(line2)
                    ret.append(line2)
                if i >= len(words):
                    for _ in range(maxWidth-sum):
                        line += " "
                    ret.append(line)
            else:
                i -= 1
                line = line.split()
                sum -= len(line[-1])
                line = line[:len(line)-1]
                x = maxWidth - sum + len(line)
                index = 0
                while x > 0:
                    if len(line) == 1:
                        line[index] += " "
                    else:
                        line[index] += " "
                        index += 1
                        index = index % (len(line)-1)
                    x -= 1
                line2 = "".join(line)

                ret.append(line2)
        return ret
t = Solution()
print t.fullJustify([""], 1)