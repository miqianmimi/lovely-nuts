# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def lengthy(c,i,L):
            if c.left:
                print("left",i)
                lengthy(c.left,i+1,L)
                if i not in L:
                    L.append(i)
            if c.right:
                print("right",i)
                lengthy(c.right,i+1,L)
                if i not in L:
                    L.append(i)
        if not root:
            return(0)
        else:
            if root.left or root.right:
                L=[]
                i=1
                lengthy(root,i,L)
                print(L)
                print(max(L)+1)
                return(max(L)+1)
            else:
                return(1)

    def maxDepth2(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))