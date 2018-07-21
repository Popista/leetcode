
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return
        if head.next == None:
            return head
        val = head.val
        node = head.next
        if node.val != val:
            head.next = self.deleteDuplicates(node)
            return head
        else:
            while node and node.val == val:
                node = node.next
            head.next = self.deleteDuplicates(node)
            return head



