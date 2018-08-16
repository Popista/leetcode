# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # dict = {}
        # node = head
        # while node:
        #     if node.val not in dict:
        #         dict[node.val] = [node]
        #     else:
        #         dict[node.val].append(node)
        #     node = node.next
        # keys = sorted(dict.keys())
        # thead = ListNode(0)
        # last = thead
        # for i in keys:
        #     for j in range(len(dict[i])):
        #         last.next = dict[i][j]
        #         last = dict[i][j]
        # last.next = None
        # return thead.next
        thead = ListNode(0)
        thead.next = head
        node = head.next
        while node:
            tmp = thead
            while tmp.next and tmp.next.val < node.val:
                tmp = tmp.next
            next = node.next
            tnext = tmp.next
            tmp.next = node
            node.next = tnext
            node = next
        return thead.next
t = Solution()
t1 = ListNode(-1)
t2 = ListNode(5)
t3 = ListNode(3)
t4 = ListNode(4)
t5 = ListNode(0)
t1.next = t2
t2.next = t3
t3.next = t4
t4.next = t5
print t.insertionSortList(t1).next.next.next.next.val

