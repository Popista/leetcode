# Definition for a  binary tree node
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator(object):
    l = []
    index = 0
    def Tree2List(self, node):
        if node == None:
            return

        self.Tree2List(node.left)
        self.l.append(node.val)

        self.Tree2List(node.right)
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.l = []
        self.Tree2List(root)
        self.index = 0
        print self.l

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.index < len(self.l):
            return True
        else:
            return False

    def next(self):
        """
        :rtype: int
        """
        ret = self.l[self.index]
        self.index += 1
        return ret

t1 = TreeNode(2)
t2 = TreeNode(1)
t3 = TreeNode(3)
t1.left = t2
t1.right = t3
t = BSTIterator(t1)
v = []
while t.hasNext():
    v.append(t.next())
print v
# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())