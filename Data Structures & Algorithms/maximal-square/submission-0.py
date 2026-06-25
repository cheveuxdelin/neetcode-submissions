class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        dp = [[0] * m for _ in range(n)]
        best = 0

        for i in range(n):
            if matrix[i][-1] == "1":
                dp[i][-1] = 1
                best = 1
        for j in range(m):
            if matrix[-1][j] == "1":
                dp[-1][j] = 1
                best = 1
        
        for i in reversed(range(n-1)):
            for j in reversed(range(m-1)):
                if matrix[i][j] == "1":
                    down = dp[i+1][j]
                    right = dp[i][j+1]
                    diagonal = dp[i+1][j+1]
                    dp[i][j] = 1 + min(down, right, diagonal)
                    best = max(best, dp[i][j])
        return best * best