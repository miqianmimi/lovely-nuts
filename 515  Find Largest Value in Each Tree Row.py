# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        maxes = []
        row = [root]
        while any(row):
            maxes.append(max(node.val for node in row))

            row = [kid for node in row for kid in (node.left, node.right) if kid]
        return maxes

    def shorttolong(self,row):
        row2 = []
        for node in row:
            for kid in (node.left, node.right):
                if kid:
                    row2.append(kid)
        row = row2
        

    def error(self,root):
        List=[]
        List.append(root)

        a = [None] * 10086
        j = 2  # j for layer
        a[0] = root
        a[1] = root.left if root.left else []
        a[2] = root.right if root.right else []
        while True:
            i = 2 ** (j - 1)  # i=2-3 #j=2
            while i >= 2 ** (j - 1) and i <= 2 ** j - 1:
                if a[i - 1] != [] and a[i - 1]:
                    a[2 * i - 1] = a[i - 1].left if a[i - 1].left else []
                    a[2 * i] = a[i - 1].right if a[i - 1].right else []
                i = i + 1
            i = 2 ** (j - 1)
            count = 0
            while i >= 2 ** (j - 1) and i <= 2 ** j - 1:
                if a[i] != () and a[i]:
                    count = count + 1
                i = i + 1
            if count == 0:
                break
            j = j + 1
        a=a[:i-1]
        b = []
        for i in a:
            if i != [] and i:
                b.append(i.val)
            if i == [] :
                b.append(-100000001)
            if i==None:
                b.append(-100000000)
        j = 1
        c = []
        while True:
            c.append( max(b[2 ** (j - 1)-1:2 ** j - 1]))
            j = j + 1
            if  2 ** j - 1 == len(b):
                break
        return(c)




