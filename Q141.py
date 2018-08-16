# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        tmp = head
        while tmp:
            if tmp.next == head:
                return True
            else:
                t = tmp.next
                tmp.next = head
                tmp = t
        return False