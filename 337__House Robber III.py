# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        list1 = []
        list2 = []
        if not root:
            return 0
        a = root
        list1.append(a.val)
        node = []
        node.append([a, 1])
        while node:
            for [i, j] in node:
                if j == 1:

                    if i.left:
                        list2.append(i.left.val)
                        node.append([i.left, 0])
                    if i.right:
                        list2.append(i.right.val)
                        node.append([i.right, 0])
                elif j == 0:
                    if i.left:
                        list1.append(i.left.val)
                        node.append([i.left, 1])
                    if i.right:
                        list1.append(i.right.val)
                        node.append([i.right, 1])
                print(1)
                node.remove([i, j])

        print(list1, list2)
        return sum(list1) if sum(list1) > sum(list2) else sum(list2)

#我这个是一行隔一行取的

#DFS
#Easy understanding solution with dfs
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def dfs(x):
            if not x:
                return [0, 0]
            left = dfs(x.left)
            right = dfs(x.right)
            res = [0, 0]
            res[0] = left[1] + right[1] + x.val
            res[1] = max(left[0], left[1]) + max(right[0], right[1])
            return res

        num = dfs(root)
        return max(num[0], num[1])
        # 存一个num[0],num[1]; num[0]是挖掘这个node的话，最大的值，num[1]是不挖掘这个Node最大的值

