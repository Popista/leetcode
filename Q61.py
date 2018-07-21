# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None:
            return None
        tmp = head
        count = 0
        while tmp.next != None:
            count += 1
            tmp = tmp.next
        tail = tmp
        count += 1
        k = k % count
        if k == 0:
            return head
        m = count - k
        tmp = head
        i = 0
        while i < m - 1:
            tmp = tmp.next
            i += 1
        left = tmp
        right = tmp.next
        tail.next = head
        left.next = None
        return right



a5 = ListNode(5)
a4 = ListNode(4)
a3 = ListNode(3)
a2 = ListNode(2)
a1 = ListNode(1)
a1.next = a2
# a2.next = a3
# a3.next = a4
# a4.next = a5
t = Solution()
ret = t.rotateRight(a1,3)
while ret != None:
    print ret.val
    ret = ret.next
