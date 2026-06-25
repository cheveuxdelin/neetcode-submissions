class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        dp = [0] * m
        dp[0] = grid[0][0]
        for i in range(1, m):
            dp[i] = dp[i-1] + grid[0][i]
        
        for i in range(1, n):
            for j in range(m):
                if j == 0:
                    dp[j] += grid[i][0]
                else:
                    dp[j] = grid[i][j] + min(dp[j], dp[j-1])
        return dp[-1]
