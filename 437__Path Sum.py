# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def pathSum(self, root, sum ):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if not root:
            return 0
        return self.dfs(root, sum)+self.pathSum(root.left, sum)+self.pathSum(root.right,sum)

    def dfs(self, root, sum ):
        res=0
        if not root:
            return res
        if sum == root.val :
            res += 1
        res += self.dfs(root.left,sum-root.val)
        res += self.dfs(root.right,sum-root.val)
        return res


