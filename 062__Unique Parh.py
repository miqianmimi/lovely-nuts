class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        m = m - 1
        n = n - 1
        c = m + n
        k = 1
        nominator = 1
        for i in range(n):
            k = k * (m + n - i)
            nominator = nominator * (i + 1)

        print(k, nominator)
        return (int(k / nominator))
