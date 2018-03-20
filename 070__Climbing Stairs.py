class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            return 2

        if n == 0:
            return 0
        m = []
        m.extend([0, 1, 2])
        for i in range(n - 1):
            a = m[i + 2] + m[i + 1]
            m.append(a)
        print(m[n])
        return (m[n])