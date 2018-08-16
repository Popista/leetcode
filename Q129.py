# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    ret = 0
    def traverse(self, node, num):
        if node is None:
            return
        num = num * 10 + node.val
        if node.left is None and node.right is None:
            self.ret += num
            return
        self.traverse(node.left, num)
        self.traverse(node.right, num)
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.traverse(root, 0)
        return self.ret
t = Solution()
t1 = TreeNode(4)
t2 = TreeNode(9)
t3 = TreeNode(5)
t4 = TreeNode(1)
t5 = TreeNode(0)
t1.left = t2
t2.left = t3
t2.right = t4
t1.right = t5
print t.sumNumbers(t1)