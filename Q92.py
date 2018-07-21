class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    # def reverseBetween(self, head, m, n):
    #     """
    #     :type head: ListNode
    #     :type m: int
    #     :type n: int
    #     :rtype: ListNode
    #     """
    #     tmp = head
    #     count = 1
    #     if m == n:
    #         return head
    #     flag = 0
    #     if m == 1:
    #         first = tmp
    #         firstRight = first.next
    #         firstLeft = None
    #         flag = 1
    #     while tmp != None:
    #         if count == n - 1:
    #             secondLeft = tmp
    #             second = tmp.next
    #             if second.next == None:
    #                 secondRight = None
    #             else:
    #                 secondRight = second.next
    #             break
    #         if flag == 0:
    #             if count == m - 1:
    #                 firstLeft = tmp
    #                 first = tmp.next
    #                 firstRight = first.next
    #         count += 1
    #         tmp = tmp.next
    #
    #
    #

        # if firstLeft == None:
        #     head = second
        #     head.next = firstRight
        #     if secondRight == None:
        #         secondLeft.next = first
        #         secondLeft.next.next = None
        #     else:
        #         secondLeft.next = first
        #         secondLeft.next.next = secondRight
        # else:
        #     firstLeft.next = second
        #     firstLeft.next.next = firstRight
        #     if secondRight == None:
        #         secondLeft.next = first
        #         secondLeft.next.next = None
        #     else:
        #         secondLeft.next = first
        #         secondLeft.next.next = secondRight
        # if second.next == second:
        #     second.next = first
        # return head
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        record = []
        tmp = head
        count = 1
        if m == n:
            return head
        left = None
        right = None
        while tmp != None:
            if count == m - 1:
                left = tmp
            if count == n + 1:
                right = tmp
                break
            if count >= m and count <= n:
                record.append(tmp)
            count += 1
            tmp = tmp.next
        if len(record) == 2:
            record[1].next = record[0]
        else:
            for i in range(len(record)-1, 0, -1):
                #print i
                record[i].next = record[i-1]
        if left == None:
            head = record[len(record)-1]
            record[0].next = right
        else:
            left.next = record[len(record)-1]
            record[0].next = right

        return head

t = Solution()
l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l5 = ListNode(5)
l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5
# tmp = l1
# while tmp != None:
#     print tmp.val
#     tmp = tmp.next
a = t.reverseBetween(l1, 1, 5)
while a != None:
    print a.val
    a = a.next