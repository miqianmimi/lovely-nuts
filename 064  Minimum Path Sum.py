class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        for i,Row in enumerate(grid):
            for j,_ in enumerate(Row):
                if[i,j]==[0,0]: continue
                if i==0: grid[i][j]=grid[i][j]+grid[i][j-1]
                elif j==0:grid[i][j]=grid[i-1][j]+grid[i][j]
                else: grid[i][j]+=min(grid[i-1][j],grid[i][j-1])
        return grid[-1][-1]
