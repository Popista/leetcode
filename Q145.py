# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret = []
        q = []
        tmp = root
        while q or tmp:
            if tmp:
                q.append(tmp)
                ret.insert(0, tmp.val)
                tmp = tmp.right
            else:
                tmp = q.pop()
                tmp = tmp.left
        return ret
t = Solution()
t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t1.right = t2
t2.left = t3
print t.postorderTraversal(t1)