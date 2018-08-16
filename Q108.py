# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildBST(self, nums):
        if len(nums) == 0 or nums is None:
            return None
        i = len(nums) / 2
        root = TreeNode(nums[i])
        left = self.buildBST(nums[:i])
        right = self.buildBST(nums[i+1:])
        root.left = left
        root.right = right
        return root
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.buildBST(nums)
t = Solution()
root = t.sortedArrayToBST([-10,-3,0,5,9])
print root.right.left.val