# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        nodeA, nodeB = headA, headB
        while nodeA != nodeB:
            if nodeA == None:
                nodeA = headB
            else:
                nodeA = nodeA.next
            if nodeB == None:
                nodeB = headA
            else:
                nodeB = nodeB.next
        return nodeA
t = Solution()
t11 = ListNode(1)
t12 = ListNode(2)
t21 = ListNode(3)
t3 = ListNode(4)
t11.next = t12
t12.next = t3
t21.next = t3
print t.getIntersectionNode(t11, t21).val
