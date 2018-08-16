# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        if not fast or not fast.next:
            return None
        t = fast.next
        n = 1
        while t != fast:
            t = t.next
            n += 1
        fast = head
        m = 0
        while m != n:
            fast = fast.next
            m += 1
        slow = head
        while fast != slow:
            slow, fast = slow.next, fast.next
        return slow
