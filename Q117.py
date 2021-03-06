# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        cur = root
        prev = None
        head = None
        while cur:
            if cur.left:
                if prev:
                    prev.next = cur.left
                else:
                    head = cur.left
                prev = cur.left
            if cur.right:
                if prev:
                    prev.next = cur.right
                else:
                    head = cur.right
                prev = cur.right
            if cur.next:
                cur = cur.next
            else:
                cur = head
                head = None
                prev = None

