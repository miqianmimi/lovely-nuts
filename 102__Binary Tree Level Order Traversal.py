# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        List=[]
        i=0
        if root:
            List.append([root.val])
        else:
            return List
        i=1
        c=root
        def append(c,i,List):
            if c.left:
                if len(List)==i:
                    List.append([])
                List[i].append(c.left.val)
                append(c.left,i+1,List)
            if c.right :
                if len(List)==i:
                    List.append([])
                List[i].append(c.right.val)
                append(c.right,i+1,List)

        append(c,1,List)
        print(List)
        return(List)

    def levelOrder2(self, root):
        ans, level = [], [root]
        while root and level:
            ans.append([node.val for node in level])
            level = [kid for n in level for kid in (n.left, n.right) if kid]
        return ans