# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if self.match(s, t): return True
        if not s: return False
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def match(self, a, b):
        if not a or not b:
            return a is b
        if a.val == b.val:
            c = self.match(a.left, b.left)
            d = self.match(a.right, b.right)
            return c and d

