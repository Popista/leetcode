# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        dict = {}
        i = 0
        tmp = head
        while tmp:
            dict[i] = tmp
            i += 1
            tmp = tmp.next
        i, j = 0, len(dict) - 1
        while 1:
            if i == j - 1:
                dict[j].next = None
                return
            elif i == j:
                dict[j].next = None
                return
            else:
                t = dict[i].next
                dict[i].next = dict[j]
                dict[j].next = t
            i += 1
            j -= 1
t = Solution()
t1 = ListNode(1)
t2 = ListNode(2)
t3 = ListNode(3)
t4 = ListNode(4)
t5 = ListNode(5)
t1.next = t2
t2.next = t3
t3.next = t4
t4.next = t5
print t.reorderList(t1)
