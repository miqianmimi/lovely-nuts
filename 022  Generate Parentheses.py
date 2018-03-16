class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return []

        def help( l, r, item, res):
            if r < l:
                return
            if l == 0 and r == 0:
                res.append(item) #加一个
            if l > 0:
                help(l - 1, r, item + '(', res)
            if r > 0:
                help(l, r - 1, item + ')', res)

        res = []
        help(n, n, '', res)
        return res


A=Solution()
B=A.generateParenthesis(3)
print (B)
