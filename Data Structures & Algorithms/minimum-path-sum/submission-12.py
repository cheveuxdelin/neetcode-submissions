class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        dp = [row.copy() for row in grid]

        for i in range(1, n):
            dp[i][0] += dp[i-1][0]
        for j in range(1, m):
            dp[0][j] += dp[0][j-1]
        

        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] += min(
                    dp[i][j-1],
                    dp[i-1][j]
                )
        return dp[-1][-1]