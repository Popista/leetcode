# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret = []
        def traverse(node):
            if not node:
                return
            ret.append(node.val)
            traverse(node.left)
            traverse(node.right)
        traverse(root)
        return ret
t = Solution()
t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t1.right = t2
t2.left = t3
print t.preorderTraversal(t1)