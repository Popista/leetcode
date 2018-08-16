# Definition for a binary tree node.
import copy
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        while root:
            if root.left:
                t = root.left
                while t.right:
                    t = t.right
                t.right = root.right
                root.right = root.left
                root.left = None
            root = root.right
t = Solution()
t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t1.left = t2
t1.right = t3
t.flatten(t1)
print t1.right.right.val