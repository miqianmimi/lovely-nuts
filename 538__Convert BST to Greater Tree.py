# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        LI = []
        c = []
        c.append(root)
        while c != []:
            # print(c)
            i = c[0]
            LI.append(i.val)
            c.remove(i)
            if i.left:
                c.append(i.left)
            if i.right:
                c.append(i.right)
        LI.sort()
        # print(LI)
        d = []
        d.append(root)
        pp = LI
        while d != []:
            # print(d)
            a = d[0]
            i = pp.index(a.val)
            sunday = pp[i + 1:]
            a.val = sum(sunday) + a.val
            d.remove(a)
            if a.left:
                d.append(a.left)
            if a.right:
                d.append(a.right)
        return (root)

#We first traverse the tree “inorder” and keep track of all values. This will be all values in the tree in ascending order.
#We then traverse the tree “reverse inorder” and set our node values as the suffix sums of values we have found.

def convertBST(self, root):
    def visit1(root):
        if root:
            visit1(root.left)
            vals.append(root.val)
            visit1(root.right)

    vals = []
    visit1(root)

    self.s = 0

    def visit2(root):
        if root:
            visit2(root.right)#给最右面最下面的加的最少
            self.s += vals.pop()
            root.val = self.s
            visit2(root.left)

    visit2(root)

    return root


