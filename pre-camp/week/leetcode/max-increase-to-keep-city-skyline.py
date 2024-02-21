class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        ans = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        maxrow = []
        maxcol = []
        result = 0

        for i in range(len(grid)):
            maxrow.append(max(grid[i]))
            maxi=0
            for j in range(len(grid)):
                maxi = max(maxi,grid[j][i])
            maxcol.append(maxi)

        for i in range(len(grid)):
            for j in range(len(grid)):
                ans[i][j]=min(maxrow[i],maxcol[j])

        for i in range(len(grid)):
            for j in range(len(grid)):
                result += ans[i][j] - grid[i][j]

        
        return result
