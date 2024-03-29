class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        maxsum = 0
        for row in range(len(grid)-2):
            for col in range(len(grid[row])-2):
                sums = grid[row][col] + grid[row][col+1] + grid[row][col+2]
                sums+= grid[row+1][col+1]
                sums+=grid[row+2][col]+ grid[row+2][col+1] + grid[row+2][col+2]
                maxsum = max(maxsum,sums)
        return maxsum
        