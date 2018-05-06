class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        r = 1
        if n == 0:
            return (r)
        if n == 1:
            return (x)
        is_negative = 0 if n > 0 else 1
        if n < 0:
            n = -1 * (n)

        half = self.myPow(x, n // 2)
        a = half * half if n % 2 == 0 else x * half * half

        return a if is_negative == 0 else 1 / a

