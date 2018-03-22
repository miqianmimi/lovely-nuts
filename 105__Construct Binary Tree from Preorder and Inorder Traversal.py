# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """

        def build(preorder, inorder, preIndex, startInIndex, endInIndex):
            if endInIndex < startInIndex:
                return None
            node = TreeNode(preorder[preIndex])
            # print(node)
            index = getIndexInInorder(inorder, preorder[preIndex])
            lenL = index - startInIndex
            lenR = endInIndex - startInIndex - lenL

            if lenL > 0:
                node.left = build(preorder, inorder, preIndex + 1, startInIndex, index - 1)
            if lenR > 0:
                node.right = build(preorder, inorder, preIndex + lenL + 1, index + 1, endInIndex)
            return (node)

        def getIndexInInorder(inorder, val):
            for i in range(len(inorder)):
                if val == inorder[i]:
                    return (i)
            return (-1)

        null = None
        if preorder and len(preorder) == 0:
            return null
        if inorder and len(inorder) == 0:
            return null
        if len(preorder) != len(inorder):
            return null
        return build(preorder, inorder, 0, 0, len(inorder) - 1)

