class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        T = []
        for m in range(1, 10):
            i = 1
            while i * i < m:
                i = i + 1
            count = 0
            for j in range(i, 0, -1):
                while m - j * j >= 0:
                    m = m - j * j
                    count = count + 1
                if m == 0:
                    break
            T.append(count)
        print(T)
        if n <= 9:
            return T[n - 1]
        if n > 9:
            for p in range(10, n + 1):
                i = 1
                while i * i < p:
                    i = i + 1
                if i * i == p:
                    T.append(1)
                else:
                    i = i - 1
                    count = float("inf")
                    for j in range(i, 0, -1):
                        # print(j)
                        # print(p-j*j-1)
                        count = min(count, 1 + T[p - j * j - 1])
                    T.append(count)
        # print(T)
        return T[-1]

#DP 算法——6732ms
    def numSquares2(self, n):
        """
        :type n: int
        :rtype: int
        """
        T = []
        T.append(0)
        for p in range(1, n + 1):
            i = 1
            while i * i < p:
                i = i + 1
            if i * i == p:
                T.append(1)
            else:
                i = i - 1
                count = float("inf")
                for j in range(i, 0, -1):
                    # print(j)
                    # print(p-j*j)
                    count = min(count, 1 + T[p - j * j])
                    # print(count)
                T.append(count)
        # print(T)
        return T[-1]

    def numSquares3(self, n):
        """
        :type n: int
        :rtype: int
        """
        T = []
        T.append(0)
        import math
        for p in range(1, n + 1):
            count = float("inf")
            for j in range(int(math.sqrt(p)), 0, -1):
                count = min(count, 1 + T[p - j * j])
            T.append(count)
        return T[-1]

#BFS 算法



