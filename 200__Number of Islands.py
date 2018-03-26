class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0

        def dfs(grid, i, j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1':
                return
            grid[i][j] = "#"
            dfs(grid, i + 1, j)
            dfs(grid, i, j + 1)
            dfs(grid, i - 1, j)
            dfs(grid, i, j - 1)

        count = 0
        for i in range(len(grid)):  # row
            for j in range(len(grid[0])):  # Line
                if grid[i][j] == "1":
                    dfs(grid, i, j)
                    count = count + 1
        return count


