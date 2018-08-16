# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    dict = {}
    def traverse(self, node, level):
        if node == None:
            return
        if level not in self.dict:
            self.dict[level] = [node.val]
        else:
            self.dict[level].append(node.val)
        self.traverse(node.left, level + 1)
        self.traverse(node.right, level + 1)
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ret = []
        self.traverse(root, 0)
        for i in self.dict:
            ret.append(self.dict[i])
        return ret[::-1]
t = Solution()
t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t1.left = t2
t1.right = t3
print t.levelOrderBottom(t1)