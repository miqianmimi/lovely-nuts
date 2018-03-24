# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root == None:
            return None

        def getlist(root, res=[]):
            res.append(root.val)
            if root.left:
                getlist(root.left, res)
            if root.right:
                getlist(root.right, res)

        def build(res):
            root.val = res[0]
            a = root
            for i in range(len(res) - 1):
                p = TreeNode(res[i + 1])
                a.right = p
                a = a.right
            return root

        res = []
        getlist(root, res)
        print(res)

        root.val = res[0]
        if root.left:
            root.left = None
        i = 1
        while i <= len(res) - 1:
            if root.left:
                root.left = None
            if root.right:
                root.right.val = res[i]  #
                i = i + 1
                print('1', i)
                root = root.right
            else:
                temp = TreeNode(res[i])
                root.right = temp
                i = i + 1
                root = root.right
                print('2', i)

