# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    ret = False
    def traverse(self, node, tmp, sum):
        if node is None:
            return
        tmp += node.val
        if node.left is None and node.right is None:
            if sum == tmp:
                self.ret = True
        self.traverse(node.left, tmp, sum)
        self.traverse(node.right, tmp, sum)
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        self.ret = False
        self.traverse(root, 0, sum)
        return self.ret
t = Solution()
t1 = TreeNode(1)
t2 = TreeNode(3)
t3 = TreeNode(4)
t1.left = t2
t1.right = t3
print t.hasPathSum(t1, 3)