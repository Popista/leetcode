# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def traverse(self, inorder, postorder, index):
        if index >= len(postorder) or len(inorder) == 0 or inorder == None:
            return
        i = inorder.index(postorder[index])
        root = TreeNode(postorder[index])

        left = self.traverse(inorder[:i], postorder, index + (len(inorder) - 1 - i) + 1)
        right = self.traverse(inorder[i+1:], postorder, index + 1)
        root.left = left
        root.right = right
        return root
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        p = postorder[::-1]
        return self.traverse(inorder, p, 0)
t = Solution()
root = t.buildTree([-4,-10,3,-1,7,11,-8,2],
[-4,-1,3,-10,11,-8,2,7])
print root.left.val