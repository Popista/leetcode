# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        num = []
        tmp = head
        while tmp != None:
            num.append(tmp)
            tmp = tmp.next
        a = len(num) - n
        if a == 0:
            return num[0].next
        if num[a].next == None:
            if len(num) == 1:
                return None
            num[a - 1].next = None
        else:
            num[a - 1].next = num[a + 1]
        return num[0]

head = ListNode(1)
# a = ListNode(2)
# b = ListNode(3)
# c = ListNode(4)
# d = ListNode(5)
# head.next = a
# a.next = b
# b.next = c
# c.next = d
t = Solution()
x = t.removeNthFromEnd(head, 1)
while x != None:
    print x.val
    x = x.next
