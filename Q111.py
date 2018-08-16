# Definition for a binary tree node.
import copy
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    minLevel = float("inf")
    def getMinDepth(self, node, level):
        if node is None:
            return
        if node.left is None and node.right is None:
            if level < self.minLevel:
                self.minLevel = level
        self.getMinDepth(node.left, level + 1)
        self.getMinDepth(node.right, level + 1)
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        self.minLevel = float("inf")
        self.getMinDepth(root, 1)
        return self.minLevel
t = Solution()
t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t4 = TreeNode(4)
t5 = TreeNode(5)
t1.left = t2
t2.left = t3
t1.right = t4
t4.right = t5
print t.minDepth(t1)