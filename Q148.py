# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def merge(l1, l2):
            p = ListNode(0)
            t = p
            while l1 and l2:
                if l1.val < l2.val:
                    t.next = l1
                    l1 = l1.next
                else:
                    t.next = l2
                    l2 = l2.next
                t = t.next
            if l1:
                t.next = l1
            if l2:
                t.next = l2
            return p.next

        if not head or not head.next:
            return head
        slow, fast = head, head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None
        l1 = self.sortList(head)
        l2 = self.sortList(slow)
        return merge(l1, l2)
t = Solution()
t1 = ListNode(3)
t2 = ListNode(2)
t3 = ListNode(1)
t1.next = t2
t2.next = t3
print t.sortList(t1).next.next.next

