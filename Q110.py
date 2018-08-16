# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    ret = True
    def traverse(self, node, level):
        if node is None:
            return 0
        l = self.traverse(node.left, level + 1)
        r = self.traverse(node.right, level + 1)
        if abs(l - r) > 1:
            self.ret = False
        return 1 + max(l, r)
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.ret = True
        self.traverse(root, 0)
        return self.ret
t = Solution()
t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t4 = TreeNode(4)
t5 = TreeNode(5)
t6 = TreeNode(6)
t7 = TreeNode(7)
t1.left = t2
t1.right = t3
t2.left = t4
t2.right = t5
t4.left = t6
t4.right = t7
print t.isBalanced(t1)