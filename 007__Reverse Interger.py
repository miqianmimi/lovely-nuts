class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x = str(x)
        y = ''
        for i in x:
            y = i + y
        print(y)
        if y[-1] == '-':
            y = '-' + y[:-1]

        y = int(y)

        if int(y) > (2147483648) or int(y) < -(2147483648):
            return (0)
        else:
            return (y)
