class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return[]
        print(root.val)
        return self.inorderTraversal(root.left) +[root.val] +self.inorderTraversal(root.right)