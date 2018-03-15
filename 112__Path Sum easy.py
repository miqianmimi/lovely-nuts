class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def hasPathSum(self, root, sum):
        #print(1)
        if root!=None:
            print(root.val)
        if not root:
            return False

        if root.val == sum and not root.left and not root.right:
            return True

        return self.hasPathSum(root.left, sum - root.val) or \
               self.hasPathSum(root.right, sum - root.val)

root = TreeNode(5)
a1 = TreeNode(4)
root.left = a1


b1 = TreeNode(11)
a1.left = b1
c1 = TreeNode(7)
c2 = TreeNode(2)
b1.right = c2
b1.left = c1

a2 = TreeNode(8)
root.right = a2
b2 = TreeNode(13)
b3 = TreeNode(4)
a2.left = b2
a2.right = b3
c3 = TreeNode(1)
b3.right = c3





a = Solution()
b = a.hasPathSum(root, sum=22)
print(b)

