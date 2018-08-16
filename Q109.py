# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def toBST(self, head, tail):
        if head == tail:
            return None
        i, j = head, head
        while i != tail and i.next != tail:
            i = i.next.next
            j = j.next
        root = TreeNode(j.val)
        left = self.toBST(head, j)
        right = self.toBST(j.next, tail)
        root.left = left
        root.right = right
        return root
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if head is None:
            return None
        return self.toBST(head, None)
# [-10,-3,0,5,9]
l1 = ListNode(-10)
l2 = ListNode(-3)
l3 = ListNode(0)
l4 = ListNode(5)
l5 = ListNode(9)
l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5
t = Solution()
root = t.sortedListToBST(l1)
print root.right.val


