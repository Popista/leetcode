# Definition for binary tree with next pointer.
#      1 -> NULL
#    /  \
#   2 -> 3 -> NULL
#  / \  / \
# 4->5->6->7 -> NULL
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution():
    # @param root, a tree link node
    # @return nothing
    def traverse(self, left, right):
        if left is None and right is None:
            return
        left.next = right
        if left.right and right.left:
            left.right.next = right.left
        if right.next and right.right and right.next.left:
            right.right.next = right.next.left
        self.traverse(left.left, left.right)
        self.traverse(right.left, right.right)
    def connect(self, root):
        if root is None:
            return
        if root.left is None:
            return
        self.traverse(root.left, root.right)
t = Solution()
t1 = TreeLinkNode(1)
t2 = TreeLinkNode(2)
t3 = TreeLinkNode(3)
t4 = TreeLinkNode(4)
t5 = TreeLinkNode(5)
t6 = TreeLinkNode(6)
t7 = TreeLinkNode(7)
t1.left = t2
t1.right = t3
t2.left = t4
t2.right = t5
t3.left = t6
t3.right = t7
t.connect(t1)
print t4.next.next.next.next










