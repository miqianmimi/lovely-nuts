class Solution:
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """

        li = board
        n = len(li)
        m = len(li[0])
        if n == 1 and m == 1:
            neigbhour = 0
            li[0][0] = 0
            board = li
            return (None)
        if [n, m] in ([2, 1], [1, 2]):
            for i in range(n):
                for j in range(m):
                    li[i][j] = 0
            board = li
            print(board)
            return (None)
        if n == 1 and m >= 3:
            kk = [None] * (m - 2)
            for j in range(m - 2):
                kk[j] = li[0][j] + li[0][j + 2]
            for i in range(m - 2):
                if kk[i] < 2:
                    li[0][i + 1] = 0
            li[0][0] = 0
            li[0][m - 1] = 0
            board = li
            print(board)
            return (None)
        if m == 1 and n >= 3:
            kk = [None] * (n - 2)
            for j in range(n - 2):  # 1,3
                kk[j] = li[j][0] + li[j + 2][0]
            for i in range(n- 2):
                if kk[i] < 2:
                    li[i + 1][0] = 0
            li[0][0] = 0
            li[n - 1][0] = 0
            print(li)
            board = li
            print(board)
            return (None)

        def count(i, j, m, n):
            count = 0
            if [i, j] == [0, 0]:
                count = count + li[i + 1][j] + li[i + 1][j + 1] + li[i][j + 1]
            elif [i, j] == [0, m - 1]:
                count = count + li[i][j - 1] + li[i + 1][j - 1] + li[i + 1][j]
            elif [i, j] == [n - 1, 0]:
                count = count + li[i - 1][j] + li[i - 1][j + 1] + li[i][j + 1]
            elif [i, j] == [n - 1, m - 1]:
                count = count + li[i - 1][j] + li[i][j - 1] + li[i - 1][j - 1]
            elif i == 0:
                count = count + li[i][j - 1] + li[i + 1][j - 1] + li[i + 1][j] + li[i][j + 1] + li[i + 1][j + 1]
            elif j == 0:
                count = count + li[i - 1][j] + li[i - 1][j + 1] + li[i][j + 1] + li[i + 1][j + 1] + li[i + 1][j]
            elif i == n - 1:
                count = count + li[i - 1][j] + li[i][j - 1] + li[i - 1][j - 1] + li[i - 1][j + 1] + li[i][j + 1]
            elif j == m - 1:
                count = count + li[i - 1][j] + li[i][j - 1] + li[i - 1][j - 1] + li[i + 1][j - 1] + li[i + 1][j]
            else:
                count = count + li[i - 1][j] + li[i - 1][j - 1] + li[i - 1][j + 1] + li[i][j - 1] + li[i][j + 1] + \
                        li[i + 1][j - 1] + li[i + 1][j] + li[i + 1][j + 1]
            return (count)

        change = []
        remain = []
        for i in range(n):
            for j in range(m):
                if count(i, j, m, n) < 2:
                    # 1
                    if li[i][j] == 1:
                        change.append([i, j])
                if count(i, j, m, n) > 3:
                    # 3
                    if li[i][j] == 1:
                        change.append([i, j])
                if count(i, j, m, n) == 2 or count(i, j, m, n) == 3:
                    # 3
                    if li[i][j] == 1:
                        remain.append([i, j])

                if count(i, j, m, n) == 3:
                    if li[i][j] == 0:
                        change.append([i, j])
        for [i, j] in change:
            li[i][j] = 1 if li[i][j] == 0 else 0

        print(li)
        board = li
        return (None)


a=Solution()
b=a.gameOfLife([[1],[0],[0],[1],[0],[0],[1],[0],[0],[1]])




