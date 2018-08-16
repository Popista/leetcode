# Definition for a binary tree node.a
import copy
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    ret = []
    def traverse(self, node, l, sum):
        if node is None:
            return
        l.append(node.val)
        print l
        if node.left is None and node.right is None:
            tmp = 0
            for i in l:
                tmp += i
            if tmp == sum:
                self.ret.append(copy.deepcopy(l))
        self.traverse(node.left, l, sum)
        self.traverse(node.right, l, sum)
        l.pop()
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        self.ret = []
        self.traverse(root, [], sum)
        return self.ret
t = Solution()
t1 = TreeNode(1)
t2 = TreeNode(3)
t3 = TreeNode(4)
t4 = TreeNode(3)
t1.left = t2
t1.right = t3
t2.right = t4
print t.pathSum(t1, 7)