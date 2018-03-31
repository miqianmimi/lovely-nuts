class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        li=[]
        a=[]
        b=[]
        def visit(root):
            if root:
                li.append(root.val)
                a.append(1) #"↙️往回2"
                print(1,root.val)
                visit(root.left)
                a.append(2)#"↘️往回3"
                print(2,root.val)
                visit(root.right)
                a.append(3) #"完成一组，123"
                print(3,root.val)
        visit(root)
        print(li)
        print(a)
        print(b)

    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None

class Solution2(object):
    def diameterOfBinaryTree2(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def depth(root):
            if not root:
                return 0
            left = depth(root.left)
            right = depth(root.right)
            self.m = max(self.m, left + right)
            print(left, right)
            return max(left, right) + 1

            # Let’s calculate the depth of a node in the usual way: max(depth of node.left, depth of node.right) + 1. While we do, a path “through” this node uses 1 + (depth of node.left) + (depth of node.right) nodes. Let’s search each node and remember the highest number of nodes used in some path. The desired length is 1 minus this number.

        self.m = 0
        depth(root)
        print(self.m)
        return self.m

